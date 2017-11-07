#!/bin/bash

$PYTHON setup.py install
mkdir -p $PREFIX/share/jupyter/nbextensions/
cp -r static/pivot-ajax $PREFIX/share/jupyter/nbextensions/
cp -r static/pivottable $PREFIX/share/jupyter/nbextensions/