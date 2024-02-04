.. QgridNext documentation master file, created by
   sphinx-quickstart on Mon Feb  5 02:44:04 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: https://raw.githubusercontent.com/zhihanyue/QgridNext/main/docs/_static/qgridnext_logo.png
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
