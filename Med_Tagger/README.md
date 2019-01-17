# Python wrapper for the SPACCC_POS-Tagger

## Introduction

This software is a wrapper around the modified FreeLing 3.1 tagger for medical terms in Spanish.


## Prerequisites

To utilize this wrapper, one has to download and compile the adapted FreeLing3.1 in Spanish for the medical domain.
Instructions can be found in the parent folder


## Directory structure

* `Med_Tagger`:  source for the Tagger wrapper
* `setup.py`: Python setup configuration files
* `README.md`: This file
* `Example.ipynb`: Jupyter Notebook with usage example

## Install

Clone this folder to your computer an run: `python setup.py install`


## Examples

To execute the program, given a text, one can use the following command:
```python
from Med_Tagger import Med_Tagger
tag = Med_Tagger() # Starts a docker image in background
results = tag.parse('Este es un texto de prueba.')

# To kill the docker image
del(tag)
```

## Contact

Felipe Soares (felipe.soares@bsc.es)

## License

(This is so-called MIT/X License)

Copyright (c) 2017-2018 Secretaría de Estado para el Avance Digital (SEAD)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
