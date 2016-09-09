"%PYTHON%" setup.py install --old-and-unmanageable

mkdir %SP_DIR%/notebook
mkdir %SP_DIR%/notebook/static
cp -r static/ajax %SP_DIR%/notebook/static
cp -r static/pivottable %SP_DIR%/notebook/static

if errorlevel 1 exit 1