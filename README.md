# SPACCC_POS-TAGGER: Spanish Clinical Case Corpus Part-of-Specch Tagger

## Introduction

This repository contains the Part-of-Speech Tagger for medical terms in Spanish based on FreeLing3.1.
It also contains the Python wrapper for this software, aiming at easier use.

## Prerequisites

To use the adapted FreeLing 3.1 to the medical domain, the following resources are required:
* Docker (https://www.docker.com/))
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
* `CNIO_Tagger`: Folder containing the Python wrapper for this tool

## Usage

To compile the adapted FreeLing3.1 docker image, the following command (from this directory) has to be executed:

```bash
$> bash compila_freeling.sh
```
The result will be the docker image  `freeling-cnio:1.0.0`

## Examples

To execute the program, given a text, one can use the following command:
```bash
$> echo 'Este es un texto de prueba.' | bash llamada_freeling.sh
```

## Python wrapper

Check the `CNIO_Tagger` folder inside this directory

## Contact

Felipe Soares (felipe.soares@bsc.es)

## License

(This is so-called MIT/X License)

Copyright (c) 2017-2018 Secretaría de Estado para el Avance Digital (SEAD)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
