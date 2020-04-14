# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(name='multimodal-keras-wrapper',
      version='3.0.10',
      description='Wrapper for Keras with support to easy multimodal data and models loading and handling.',
      author='Marc Bolaños - Alvaro Peris',
      author_email='marc.bolanos@ub.edu',
      url='https://github.com/MarcBS/multimodal_keras_wrapper',
      download_url='https://github.com/MarcBS/multimodal_keras_wrapper/archive/master.zip',
      license='MIT',
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          "License :: OSI Approved :: MIT License"
      ],
      install_requires=['keras',
                        'numpy',
                        'six',
                        'toolz',
                        'cloudpickle',
                        'matplotlib',
                        'sacremoses',
                        'sacrebleu',
                        'scipy',
                        'future',
                        'cython',
                        'keras_applications',
                        'keras_preprocessing',
                        'sklearn',
                        'tables'
                        ],
      extras_require={
          'cython ': ['cython'],
          'tests': ['pytest',
                    'pytest-pep8',
                    'pytest-xdist',
                    'flaky',
                    'pytest-cov',
                    'requests',
                    'markdown'],
      },
      packages=find_packages())
