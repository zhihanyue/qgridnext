#!/usr/bin/env python
import os
import sys
from os.path import join

links = [
    join(sys.prefix, 'etc/jupyter/nbconfig/notebook.d/qgridnext.json'),
    join(sys.prefix, 'share/jupyter/nbextensions/qgridnext'),
    join(sys.prefix, 'share/jupyter/labextensions/qgridnext')
]
for link in links:
    if os.path.islink(link):
        print("Unlinking " + link)
        os.unlink(link)
