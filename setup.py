from setuptools import setup, find_packages, Command
from setuptools.command.sdist import sdist
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from subprocess import check_call
import os
import sys
import platform
from glob import glob
from os.path import join, dirname, abspath, exists

here = dirname(abspath(__file__))

node_root = join(here, 'js')
npm_path = os.pathsep.join([
    join(node_root, 'node_modules', '.bin'),
                os.environ.get('PATH', os.defpath),
])

with open(join(here, 'README.md'), 'r') as f:
    readme = f.read()

from distutils import log
log.set_verbosity(log.DEBUG)
log.info('setup.py entered')
log.info('$PATH=%s' % os.environ['PATH'])

def js_prerelease(command):
    """decorator for building minified js/css prior to another command"""
    class DecoratedCommand(command):
        def run(self):
            jsdeps = self.distribution.get_command_obj('jsdeps')
            if all(exists(t) for t in jsdeps.targets):
                command.run(self)
                return

            try:
                self.distribution.run_command('jsdeps')
            except Exception as e:
                missing = [t for t in jsdeps.targets if not exists(t)]
                log.warn('building js and css failed')
                if missing:
                    log.error('missing files: %s' % missing)
                raise e

            command.run(self)
            update_package_data(self.distribution)
    return DecoratedCommand

def update_package_data(distribution):
    """update package_data to catch changes during setup"""
    build_py = distribution.get_command_obj('build_py')
    # distribution.package_data = find_package_data()
    # re-init build_py options which load package_data
    build_py.finalize_options()

data_files = [
    ('etc/jupyter/nbconfig/notebook.d' , ['qgridnext.json']),
    ('share/jupyter/nbextensions/qgridnext', glob('js/static_nb/*.*')),
    ('share/jupyter/labextensions/qgridnext', glob('js/static/*.*') + ['install.json']),
    ('share/jupyter/labextensions/qgridnext/static', glob('js/static/static/*.*'))
]

class NPM(Command):
    description = 'install package.json dependencies using npm'

    user_options = []

    node_modules = join(node_root, 'node_modules')

    targets = [
        join(here, 'js', 'static'),
        join(here, 'js', 'static', 'static'),
        join(here, 'js', 'static_nb', 'extension.js'),
        join(here, 'js', 'static_nb', 'index.js')
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def has_npm(self):
        try:
            check_call(['npm', '--version'])
            return True
        except:
            return False

    def should_run_npm_install(self):
        package_json = join(node_root, 'package.json')
        node_modules_exists = exists(self.node_modules)
        return self.has_npm()

    def run(self):
        has_npm = self.has_npm()
        if not has_npm:
            log.error("`npm` unavailable.  If you're running this command using sudo, make sure `npm` is available to sudo")

        env = os.environ.copy()
        env['PATH'] = npm_path

        if self.should_run_npm_install():
            log.info("Installing build dependencies with npm. This may take a while...")
            check_call(['npm', 'install'], cwd=node_root, stdout=sys.stdout, stderr=sys.stderr)
            os.utime(self.node_modules, None)

        for t in self.targets:
            if not exists(t):
                msg = 'Missing file: %s' % t
                if not has_npm:
                    msg += '\nnpm is required to build a development version of a widget extension'
                raise ValueError(msg)

        # update package data in case this created new files
        update_package_data(self.distribution)

        # refresh data files
        global data_files
        data_files += [
            ('etc/jupyter/nbconfig/notebook.d' , ['qgridnext.json']),
            ('share/jupyter/nbextensions/qgridnext', glob('js/static_nb/*.*')),
            ('share/jupyter/labextensions/qgridnext', glob('js/static/*.*') + ['install.json']),
            ('share/jupyter/labextensions/qgridnext/static', glob('js/static/static/*.*'))
        ]
        log.info("Refreshed data files")


version_ns = {}
with open(join(here, 'qgrid', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

def read_requirements(basename):
    reqs_file = join(dirname(abspath(__file__)), basename)
    with open(reqs_file) as f:
        return [req.strip() for req in f.readlines()]

setup_args = {
    'name': 'qgridnext',
    'version': version_ns['__version__'],
    'description': 'An Interactive Grid for Sorting and Filtering DataFrames in Jupyter',
    'long_description': readme,
    'long_description_content_type': 'text/markdown',
    'include_package_data': True,
    'data_files': data_files,
    "python_requires": ">=3.7",
    'install_requires': read_requirements('requirements.txt'),
    'extras_require': {
        "test": [
            "pytest>=2.8.5",
            "flake8>=3.6.0"
        ],
    },
    'packages': find_packages(),
    'zip_safe': False,
    'cmdclass': {
        'build_py': js_prerelease(build_py),
        'egg_info': js_prerelease(egg_info),
        'sdist': js_prerelease(sdist),
        'jsdeps': NPM,
    },

    'author': 'QgridNext',
    'url': 'https://github.com/zhihanyue/qgridnext',
    'license': 'Apache-2.0',
    'keywords': [
        'ipython',
        'jupyter',
        'widgets',
    ],
    'classifiers': [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Multimedia :: Graphics',
        "Framework :: Jupyter",
        "Framework :: Jupyter :: JupyterLab",
        "Framework :: Jupyter :: JupyterLab :: 4",
        "Framework :: Jupyter :: JupyterLab :: Extensions",
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
}

setup(**setup_args)
