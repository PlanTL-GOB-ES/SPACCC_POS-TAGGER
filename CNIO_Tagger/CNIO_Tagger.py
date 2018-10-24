from __future__ import print_function
from builtins import object
import subprocess


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
    
    
    def parse(self, text):
        """
        Function to parse a single string using the tagger
        Input:
            -text: string to be tagged
        Ouput:
            -results: list of tuples containing: (original_word, lemma, tag, score)
        """
        
        results = list()
        
        self._tagger.stdin.write((text+'\n').encode('utf-8'))
        self._tagger.stdin.flush()
        
        while True:
            r = self._tagger.stdout.readline()[:-1]
            if not r:
                break
            results.append(tuple(r.decode('utf-8').split(' ')))
        
        return results
    
    
    def __del__(self):
        """
        Destroyer that will kill the background docker container
        """
        
        self._tagger.kill()
        