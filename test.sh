#!/bin/bash

virtualenv examples/venv
source examples/venv/bin/activate
python setup.py install
cd examples
python -m unittest discover
