from __future__ import print_function
from builtins import object
import subprocess
from threading import Thread
from time import sleep
from queue import Queue, Empty
import os
import unicodedata


def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))
    return s


class NonBlockingStreamReader:
    # from https://gist.github.com/EyalAr/7915597
    def __init__(self, stream):
        '''
        stream: the stream to read from.
                Usually a process' stdout or stderr.
        '''

        self._s = stream
        self._q = Queue()

        def _populateQueue(stream, queue):
            '''
            Collect lines from 'stream' and put them in 'quque'.
            '''

            while True:
                line = stream.readline()
                if line:
                    queue.put(line)
                else:
                    raise UnexpectedEndOfStream

        self._t = Thread(target=_populateQueue,
                         args=(self._s, self._q))
        self._t.daemon = True
        self._t.start()  # start collecting lines from the stream


    def readline(self, timeout=None):
        try:
            return self._q.get(block=timeout is not None,
                               timeout=timeout)
        except Empty:
            return None


class UnexpectedEndOfStream(Exception): pass



class CNIO_Tagger(object):
    """
    Wrapper around the CNIO POS tagger based on freeling
    Before calling the wrapper, one must install the dockerized version of the software
    """

    def __init__(self):
        """
        Initialize the subprocess that will receive the inputs from the user
        """
        self._tagger = subprocess.Popen('docker run -i freeling-cnio:1.0.0', shell=True,
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        sleep(2)

        self._nbsr = NonBlockingStreamReader(self._tagger.stdout)
        sleep(1)


    def get_results(self, text):
        """
        Function to get results from Freeling
        Input:
            -text: string to be tagged
        Ouput:
            -results: list of tuples
        """

        results = list()

        self._tagger.stdin.write((text + '\n').encode('utf-8'))
        self._tagger.stdin.flush()

        results = []
        while True:
            output = self._nbsr.readline(0.1)
            # 0.1 secs to let the shell output the result
            if not output:
                break
            results.append(tuple(output.decode('utf-8').split(' ')))

        return results


    def parse(self, text):
        """
        Function to parse a single string using the tagger
        Input:
            -text: string to be tagged
        Ouput:
            -results: list of tuples containing: (original_word, lemma, tag, score) if input has just one sentence
                    list of list containing the tuples for each sentence
        """

        result = self.get_results(text)

        sentences = []
        single_sentence = []

        for item in result:
            if (len(item) < 3):
                sentences.append(single_sentence)
                single_sentence = []
            else:
                single_sentence.append(item)

        if len(sentences) == 1:
            return sentences[0]
        else:
            return sentences


    def write_brat(self, parsed, folder_path):
        """
        Function to write the parsed string into BRAT format file
        Input:
            - parsed: Result from parse method
            - folder_path: Complete path to the file to be saved
        :return:
        """


        def convertirTexto(parsed, folder_path):
            ini = 0
            fin = 0
            idT = 0

            if any(isinstance(el, list) for el in parsed):
                f = open(folder_path, "w")

                # cogemos los distintos componentes de las lineas de freeling (forma, lema, etiqueta, porcentaje(despreciable))

                for item in parsed:
                    for i, s in enumerate(item):
                        item[i]= (elimina_tildes(item[i][0]), elimina_tildes(item[i][1]), elimina_tildes(item[i][2]))

                    for t in item:
                        forma = t[0]
                        lema = t[1]
                        etiqueta = t[2]
                        etiquetaSimple = etiqueta if (etiqueta[0] == 'F' or etiqueta[0] == 'Z') else etiqueta[:2]

                        # calculamos el inicio y el final de la forma en el texto
                        ini = fin
                        fin = ini + len(forma)
                        idT += 1

                        # escribimos una linea para etiquetar la palabra en brat (Tx    etiquetaSimple inicio fin    forma)
                        f.write("T" + str(idT) + "\t" + etiquetaSimple + " " + str(ini) + " " + str(fin) + "\t" +
                                forma + "\n")

                        # escribimos una linea para los comentarios de la palabra (#x    Norm Tx    lema etiqueta)
                        f.write(
                            "#" + str(idT) + "\t" + "Norm " + "T" + str(idT) + "\t" + lema + " " + etiqueta + "\n")

                        fin += 1

                f.close()

            else:
                f = open(folder_path, "w")

                for t in parsed:
                    t = (elimina_tildes(t[0]), elimina_tildes(t[1]), elimina_tildes(t[2]))

                    forma = t[0]
                    lema = t[1]
                    etiqueta = t[2]
                    etiquetaSimple = etiqueta if (etiqueta[0] == 'F' or etiqueta[0] == 'Z') else etiqueta[:2]

                    # calculamos el inicio y el final de la forma en el texto
                    ini = fin
                    fin = ini + len(forma)
                    idT += 1

                    # escribimos una linea para etiquetar la palabra en brat (Tx    etiquetaSimple inicio fin    forma)
                    f.write("T" + str(idT) + "\t" + etiquetaSimple + " " + str(ini) + " " + str(fin) + "\t" +
                            forma + "\n")

                    # escribimos una linea para los comentarios de la palabra (#x    Norm Tx    lema etiqueta)
                    f.write(
                        "#" + str(idT) + "\t" + "Norm " + "T" + str(idT) + "\t" + lema + " " + etiqueta + "\n")

                    fin += 1

                f.close()


        convertirTexto(parsed, folder_path)



    def __del__(self):
        """
        Destroyer that will kill the background docker container
        """

        self._tagger.kill()