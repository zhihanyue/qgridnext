<h1 align="center">
  <img width="230px" src="https://raw.githubusercontent.com/zhihanyue/qgridnext/main/docs/_static/qgridnext_logo.png">
</h1>
<div align="center">

[Documentation](https://qgridnext.readthedocs.io) | [Demos](https://github.com/zhihanyue/qgridnext-demos) | [Presentation](https://www.youtube.com/watch?v=AsJJpgwIX0Q) | [Changelog](https://qgridnext.readthedocs.io/en/latest/changelog.html)

</div>

<br>

Qgrid is a Jupyter widget that utilizes [SlickGrid](https://github.com/mleibman/SlickGrid) to render pandas DataFrames within JupyterLab/Notebook. This allows you to explore your DataFrames with intuitive scrolling, sorting, and filtering controls, as well as edit your DataFrames by double clicking cells. Initially developed by Quantopian, [its repo](https://github.com/quantopian/qgrid) ceased maintenance in 2020. QgridNext aims to continue maintaining and improving it for future Jupyter versions.

![filtering_demo](https://raw.githubusercontent.com/zhihanyue/qgridNext/main/docs/_static/filtering_demo.gif)

## Compatibility

QgridNext is compatible with recent versions of Jupyter:

| QgridNext |  JupyterLab  | Notebook |    Voila    |
|:---------:|:------------:|:--------:|:-----------:|
|  v2.0.0   |   v3 - v4    | v5 - v7  | v0.2 - v0.5 |

The test environments are provided in the [test_envs](https://github.com/zhihanyue/qgridnext/tree/main/test_envs) folder. You can try the widget in these environments easily.


## QgridNext V2.0.0

The first release v2.0.0 significantly improves compatibility and addresses bugs found in Qgrid v1.3.1.
* Support JupyterLab 4;
* Released as a prebuilt extension (now can be installed with one step);
* UI improvements:
  * Fix infinitely expanding width of the container in voila <= 0.3;
  * Prevent unexpected scrolling when clicking rows in Chrome for JupyterLab;
  * Adapt canvas size when the sidebar width changes in JupyterLab;
  * Fix poorly displayed left/right button of date picker;
  * Correct text color in dark mode;
  * Standardize HTML tags to fix poorly displayed filters;
* Building bug fixes:
  * Fix inconsistent pkg name for embeddable qgrid bundle;
  * Fix data_files finding that results in incomplete extension setup;
  * Fix building errors for Node >= 18;
* Other fixes:
  * Ensure `Defaults.grid_option` dict instance are not shared across widget instances;
  * Remove full-screen mode for voila compatibility;
  * Remove deprecated QGridWidget alias, only QgridWidget is allowed;
  * Replace deprecated usages for traitlets, pandas and jquery.

## Installation

Installing with pip:

```bash
pip install qgridnext
```


### Requirements

QgridNext supports Python 3.7+ and depends on the following packages:

* [pandas](https://github.com/pandas-dev/pandas) >= 0.20
* [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) >= 7
* [numpy](https://github.com/numpy/numpy)
* [traitlets](https://github.com/ipython/traitlets)


## Usage

### Exploring Dataframes

**Rendering your DataFrame:**
```py
from qgrid import show_grid
show_grid(your_df)
```
<!-- ![multi_index](https://raw.githubusercontent.com/zhihanyue/qgridNext/main/docs/_static/multi_index.png) -->

Qgrid excels in handling large DataFrames. For example, it can render a DataFrame with 10,000,000 rows in about 0.8 seconds:

![render_time](https://raw.githubusercontent.com/zhihanyue/qgridNext/main/docs/_static/render_time.png)


**Column-specific options:** Qgrid has the ability to set a number of options on a per column basis. This allows you to do things like explicitly specify which column should be sortable, editable, etc. For example, if you wanted to prevent editing on all columns except for a column named 'A', you could do the following:

```py
col_opts = { 'editable': False }
col_defs = { 'A': { 'editable': True } }
show_grid(df, column_options=col_opts, column_definitions=col_defs)
```

**Row-specific options:** Currently, Qgrid supports disabling row editing on a per-row basis, enabling row editability based on specific criteria:

```py
def can_edit_row(row):
    return row['status'] == 'active'
show_grid(df, row_edit_callback=can_edit_row)
```

**Updating an existing Qgrid widget**: You can update an existing Qgrid widget's state using APIs like [edit_cell](https://qgridnext.readthedocs.io/en/latest/api.html#qgrid.QgridWidget.edit_cell), [change_selection](https://qgridnext.readthedocs.io/en/latest/api.html#qgrid.QgridWidget.change_selection), [toggle_editable](https://qgridnext.readthedocs.io/en/latest/api.html#qgrid.QgridWidget.toggle_editable), and [change_grid_option](https://qgridnext.readthedocs.io/en/latest/api.html#qgrid.QgridWidget.change_grid_option).


### Event handlers

Use `on` and `off` methods to attach/detach event handlers. They're available on both the `qgrid` module (see [qgrid.on](https://qgridnext.readthedocs.io/en/latest/api.html#qgrid.on)) and individual `QgridWidget` instances (see [qgrid.QgridWidget.on](https://qgridnext.readthedocs.io/en/latest/api.html#qgrid.QgridWidget.on)).

Example:
```py
def handle_json_updated(event, qgrid_widget):
    # Exclude 'viewport_changed' events since that doesn't change the DataFrame
    if (event['triggered_by'] != 'viewport_changed'):
        print(qgrid_widget.get_changed_df())

# qgrid_widget = show_grid(...)
qgrid_widget.on('json_updated', handle_json_updated)
```

Alternatively, the traditional `observe` method is available but not recommended due to its less granular event control:
```py
def handle_df_change(change):
    print(change['new'])

qgrid_widget.observe(handle_df_change, names=['_df'])
```

Event handlers enable interesting integrations with other widgets/visualizations, like using qgrid to filter a DataFrame also displayed by another visualization.

![linked_to_scatter](https://raw.githubusercontent.com/zhihanyue/qgridNext/main/docs/_static/linked_to_scatter.gif)

For more examples, see the [events notebook](https://github.com/zhihanyue/qgridnext-demos/blob/master/events.ipynb).


## Troubleshoot

If you are not seeing the widget, check if the extension is installed and enabled:

```bash
jupyter labextension list
jupyter labextension enable qgridnext  # enable it if disabled
```

## Testing

Multiple test environments are provided in [test_envs](https://github.com/zhihanyue/qgridnext/tree/main/test_envs). You can perform automated tests by pytest, or manually test it in your browser.

## Development

Note: JupyterLab 4 and NodeJS are required to build the extension package. You can use `dev.yml` in [test_envs](https://github.com/zhihanyue/qgridnext/tree/main/test_envs) for a quick setup.

```bash
git clone https://github.com/zhihanyue/qgridnext
cd qgridnext
pip install -ve .  # Install package in development mode
```

`pip install -ve .` installs the package into your python environment as a symlink. It also creates symlinks of built JS extensions for your Jupyter environments automatically (implemented by our custom command in `setup.py`). After making any changes to the JS code, just rebuild it by:

```bash
npm --prefix ./js install
```

When uninstalling it, you need to clean up the JS symlinks via script `unlink_dev.py`:

```bash
pip uninstall qgridnext
python ./unlink_dev.py
```


## Contributing

All contributions, bug reports, bug fixes, documentation improvements, enhancements, demo improvements and ideas are welcome.
