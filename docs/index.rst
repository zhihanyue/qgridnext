.. QgridNext documentation master file, created by
   sphinx-quickstart on Mon Feb  5 02:44:04 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Welcome to QgridNext's documentation!
.. =====================================

.. .. toctree::
..    :maxdepth: 2
..    :caption: Contents:



.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

.. image:: https://media.quantopian.com/logos/open_source/qgrid-logo-03.png
    :target: https://qgridnext.readthedocs.io
    :width: 190px
    :align: center
    :alt: qgridnext

QgridNext API Documentation
=====================================

QgridNext is a Jupyter widget which uses `SlickGrid <https://github.com/mleibman/SlickGrid>`_ to render pandas
DataFrames within a Jupyter. This allows you to explore your DataFrames with intuitive scrolling, sorting, and
filtering controls, as well as edit your DataFrames by double clicking cells.

:mod:`qgrid` Module
-------------------

.. automodule:: qgrid
    :members:
    :exclude-members: QgridWidget

    .. autoclass:: QgridWidget(df=None, grid_options=None, precision=None, show_toolbar=None)
        :members:
