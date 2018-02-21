``pivottablejs``: the airgapped version
=======================================

This is an air-gapped version for ``pivottablejs``.

**Note**: 
An air gap, air wall or air gapping is a network security measure employed on one or more computers
to ensure that a secure computer network is physically isolated from unsecured networks, such as
the public Internet or an unsecured local area network.

Drag’n’drop Pivot Tables and Charts for `Jupyter/IPython Notebook`_,
care of `PivotTable.js`_

Installation
------------

conda install pivottablejs-airgap

Usage
-----

::

    import pandas as pd
    df = pd.read_csv("some_input.csv")

    from pivottablejs import pivot_ui

    pivot_ui(df)

.. _Jupyter/IPython Notebook: http://jupyter.org/
.. _PivotTable.js: https://github.com/nicolaskruchten/pivottable
