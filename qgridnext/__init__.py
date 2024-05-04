from ._version import __version__  # noqa F401

from .grid import (
    enable,
    disable,
    set_defaults,
    on,
    off,
    set_grid_option,
    show_grid,
    QgridWidget
)


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "static",
            "dest": "qgridnext",
            "require": "qgridnext/extension",
        }
    ]


__all__ = [
    "enable",
    "disable",
    "set_defaults",
    "on",
    "off",
    "set_grid_option",
    "show_grid",
    "QgridWidget"
]
