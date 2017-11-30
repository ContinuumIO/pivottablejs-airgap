"%PYTHON%" setup.py install

mkdir %PREFIX%/share
mkdir %PREFIX%/share/jupyter
mkdir %PREFIX%/share/jupyter/nbextensions
if errorlevel 1 exit 1

move static/pivot-ajax %PREFIX%/share/jupyter/nbextensions/
if errorlevel 1 exit 1

move static/pivottable %PREFIX%/share/jupyter/nbextensions/
if errorlevel 1 exit 1