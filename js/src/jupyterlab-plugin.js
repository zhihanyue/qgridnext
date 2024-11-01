var qgridnext = require('./index');

var base = require('@jupyter-widgets/base');

/**
 * The widget manager provider.
 */
module.exports = {
  id: 'qgridnext',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'qgridnext',
          version: qgridnext.version,
          exports: qgridnext
      });
    },
  autoStart: true
};
