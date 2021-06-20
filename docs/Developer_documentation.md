# Developer documentation

## Overview

`cmajortransposition` is an OpenSource Python module implemented using the version Python 3.8.5.
Its purpose is to transpose a sheet music to C major key.

## Getting started

### Install the dependencies

To build the project and use the python module, the following dependencies have to be installed:
* git
* python3
* python3-pip.

To run the tests, the following dependencies have to be installed:
* nose2 (with pip3).

### Build the project

The project can be set up by the following commands:
```
git clone git@github.com:soline-b/c-major-transposition.git
cd c-major-transposition
python3 setup.py build
python3 setup.py install
```

The Python module is now accessible through Python scripts or the Python console.

## Structure

The GitHub of the project presents the following structure:

```
c-major-transposition/
│
├── .github/workflows
│     └── testing.yml
|
├── docs
|     ├──images
│     |   └── <images files>
│     └── <documentation files>
|
├── src/cmajortransposition
|     ├── __init__.py
|     ├── notetools.py
│     └── sheetmusic.py
|
├── tests
|     ├──__init__.py
|     ├── test_notetools.py
│     └── test_sheetmusic.py
|
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.cfg
└── setup.py
```

## How to contribute

All there is to know to contribute is presented on the [Contribution page](Contributing.md).
