# SPACCC_POS-TAGGER: Spanish Clinical Case Corpus Part-of-Speech Tagger


## Introduction

This repository contains the Part-of-Speech Tagger for medical domain corpus in Spanish based on FreeLing3.1.
It also contains the Python wrapper for this software, aiming at easier use.

## Demo

Here you can find a demonstration of the Part-of-Speech Tagger: http://temu.bsc.es/pos/ 


## Prerequisites

To use the SPACCC_POS-TAGGER, the following resources are required:
* Docker (https://www.docker.com/)
* To have all the resources included in this directory (use git clone)
* To compile the docker container (steps detailed below)
* Be able to run docker as a non-root user (https://docs.docker.com/install/linux/linux-postinstall/)

## Directory structure

* `compila_freeling.sh`:  compiles the adapted FreeLing3.1 docker image
* `config.cfg`: FreeLing configuration file
* `Dockerfile`: Dockerfile for image compilation
* `llamada_freeling.sh`: Script to execute the analysis of a text with the adapted FreeLing 
* `README.md`: This file
* `singlewords.dat`: File with the normalized resources (words, acronyms, and abbreviations)
* `splitter.dat`: Sentence segmentantion rules
* `tokenizer.dat`: Tokenization rules
* `usermap.dat`: Rules for POS assignment (regular expressions)
* `Med_Tagger`: Folder containing the Python wrapper for this tool

## Usage

To compile the adapted FreeLing3.1 docker image, the following command (from this directory) has to be executed:

```bash
$> bash compila_freeling.sh
```
The result will be the docker image  `med-tagger:1.0.0`

## Examples

To execute the program, given a text, one can use the following command:
```bash
$> echo 'Este es un texto de prueba.' | bash llamada_freeling.sh
```
This generates an output with four columns: input wordform, lemma, PoS tags and score:

`Esto este PD0NS000 1`
`es ser VSIP3S0 1`Esto este PD0NS000 1
es ser VSIP3S0 1
un uno DI0MS0 0.987295
texto texto NCMS000 1
de de SPS00 0.999984
prueba prueba NCFS000 0.972603
. . Fp 1

`un uno DI0MS0 0.987295`
`texto texto NCMS000 1`
`de de SPS00 0.999984`
`prueba prueba NCFS000 0.972603`
`. . Fp 1`

## Performance

| Gold standard vs Tagger |   ACC  |
| ----------------------  | ------ |
| Splitting               | 98,85% |
| Tokenization            | 99,47% |
| Part-of-Speech          | 99,87% |


## Python wrapper

Check the `Med_Tagger` folder inside this directory

## Contact

Felipe Soares (felipe.soares@bsc.es)

## License

FreeLing is licensed under GPL (https://www.gnu.org/licenses/gpl-3.0.en.html). 
