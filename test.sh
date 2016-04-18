#!/bin/bash

virtualenv example/venv
source example/venv/bin/activate
python setup.py install
cd examples
python -m unittest discover
