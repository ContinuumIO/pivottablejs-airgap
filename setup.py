from distutils.core import setup


setup(
    name='pivottablejs',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',

    description='PivotTable.js integration for Jupyter/IPython Notebook',

    # The project's main homepage.
    url='https://github.com/nicolaskruchten/jupyter_pivottablejs',

    # Author details
    author='Nicolas Kruchten',
    author_email='nicolas@kruchten.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: IPython',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: JavaScript'
    ],

    # What does your project relate to?
    keywords='pivot table grid pivottable pivotgrid pivotchart crosstab',

    py_modules=["pivottablejs"]
)
