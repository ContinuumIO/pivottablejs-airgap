#!/bin/bash

$PYTHON setup.py install
mkdir $SP_DIR/notebook
mkdir $SP_DIR/notebook/static
cp -r static/ajax $SP_DIR/notebook/static
cp -r static/pivottable $SP_DIR/notebook/static