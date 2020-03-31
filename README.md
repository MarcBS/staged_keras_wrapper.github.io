# Multimodal Keras Wrapper
Wrapper for Keras with support to easy multimodal data and models loading and handling.

[![PyPI version](https://badge.fury.io/py/multimodal-keras-wrapper.svg)](https://badge.fury.io/py/multimodal-keras-wrapper) [![Build Status](https://travis-ci.org/lvapeab/multimodal_keras_wrapper.svg?branch=master)](https://travis-ci.org/lvapeab/multimodal_keras_wrapper) [![Requirements Status](https://requires.io/github/lvapeab/multimodal_keras_wrapper/requirements.svg?branch=master)](https://requires.io/github/lvapeab/multimodal_keras_wrapper/requirements/?branch=master) ![Compatibility](https://img.shields.io/badge/Python-2.7%2F3.7-blue.svg) [![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/lvapeab/multimodal_keras_wrapper/blob/master/LICENSE)

## Documentation

You can access the library documentation page at [marcbs.github.io/multimodal_keras_wrapper/](http://marcbs.github.io/multimodal_keras_wrapper/)

Some code examples are available in demo.ipynb and test.py. Additionally, in the section Projects you can see some practical examples of projects using this library.


## Installation

Assuming that you have [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) installed, run:

```
pip install multimodal-keras-wrapper
```

Alternatively, if you want to install the library from the source code, you just have to follow these steps:

1) Clone this repository.

2) Include the repository path into your PYTHONPATH:
```
export PYTHONPATH=$PYTHONPATH:/path/to/multimodal_keras_wrapper
```

3) Install the dependencies (it will install our [custom Keras fork](https://github.com/MarcBS/keras)):
```
pip install -r requirements.txt
```


## Additional dependencies

The following additional dependencies are required to fully exploit this library:

 - Keras - [custom fork](https://github.com/MarcBS/keras) or [original version](https://github.com/fchollet/keras)
 - The `cupy` package can be used for performing numpy-like operations in the GPU. If not available, the package will fall back to numpy.
 - [Coco-caption evaluation package](https://github.com/lvapeab/coco-caption/tree/master/pycocoevalcap/) (Only required to perform COCO evaluation). This package requires `java` (version 1.8.0 or newer).
 
Only when using NMS for certain localization utilities:
 - [cython](https://pypi.python.org/pypi/Cython/0.25.2) >= 0.23.4


## Projects

You can see more practical examples in projects which use this library:

[TMA for Egocentric Video Captioning based on Temporally-linked Sequences](https://github.com/MarcBS/TMA).

[NMT-Keras: Neural Machine Translation](https://github.com/lvapeab/nmt-keras).

[VIBIKNet for Visual Question Answering](https://github.com/MarcBS/VIBIKNet)

[ABiViRNet for Video Description](https://github.com/lvapeab/ABiViRNet)

[Sentence-SelectioNN for Domain Adaptation in SMT](https://github.com/lvapeab/sentence-selectioNN)


## Keras

For additional information on the Deep Learning library, visit the official web page www.keras.io or the GitHub repository https://github.com/keras-team/keras.

You can also use our [custom Keras version](https://github.com/MarcBS/keras), which provides several additional layers for Multimodal Learning.
