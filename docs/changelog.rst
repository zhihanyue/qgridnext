Changelog
=================

QgridNext V2.0.3
------------------

- Add dark theme support for JupyterLab, Notebook, and VSCode-Jupyter, automatically adapting to the environment's theme;
- Use Jupyter's default font for improved readability;
- Minor UI fixes:

  * Fix the unexpected scrolling to the top when clicking the reset button in VSCode;
  * Disable animations for date pickers;
  * Correct width of boolean filters;
  * Adjust z-index of date pickers.


QgridNext V2.0.2
------------------

- Fix errors on string columns for pandas v2.2;
- Fix the filters for numeric pyarrow columns with `NA` values;
- Ensure consistent scrollbar measurements across different environments;
- Remove an unwanted css entry causing display issues with ipywidgets.


QgridNext V2.0.1
------------------

- Support `string[pyarrow]`-typed columns;
- Deprecate `import qgrid`; now `qgrid` is an alias of `qgridnext` and is not recommended.

QgridNext V2.0.0
------------------

The first release v2.0.0 significantly improves compatibility and addresses bugs found in Qgrid v1.3.1.

- Support JupyterLab 4;
- Released as a prebuilt extension (now can be installed with one step);
- UI improvements:

  * Fix infinitely expanding width of the container in voila <= 0.3;
  * Prevent unexpected scrolling when clicking rows in Chrome for JupyterLab;
  * Adapt canvas size when the sidebar width changes in JupyterLab;
  * Fix poorly displayed left/right button of date picker;
  * Correct text color in dark mode;
  * Standardize HTML tags to fix poorly displayed filters;

- Building bug fixes:

  * Fix inconsistent pkg name for embeddable qgrid bundle;
  * Fix data_files finding that results in incomplete extension setup;
  * Fix building errors for Node >= 18;

- Other fixes:

  * Ensure `Defaults.grid_option` dict instance are not shared across widget instances;
  * Remove full-screen mode for voila compatibility;
  * Remove deprecated QGridWidget alias, only QgridWidget is allowed;
  * Replace deprecated usages for traitlets, pandas, and jquery.

