# -*- coding: utf-8 -*-

# mathtoolspy
# -----------
# A fast, efficient Python library for mathematically operations, like
# integration, solver, distributions and other useful functions.
# 
# Author:   sonntagsgesicht, based on a fork of Deutsche Postbank [pbrisk]
# Version:  0.3, copyright Saturday, 14 September 2019
# Website:  https://github.com/sonntagsgesicht/mathtoolspy
# License:  Apache License 2.0 (see LICENSE file)


import os
import sys
from auxilium import replacements_from_pkg, replacements, replacements_str

sys.path.insert(0, os.path.abspath('../../'))  #  needed to import pkg
sys.path.insert(0, os.path.abspath('.'))  #  needed to import pkg

if os.getcwd().find('readthedocs')<0:
    pkg = __import__(os.getcwd().split(os.sep)[-3])
else:
    pkg = __import__(os.getcwd().split(os.sep)[-5])

sys.path.insert(0, os.path.abspath('../../' + pkg.__name__))  #  needed to import pkg

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    #'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
]

autodoc_default_options = {
    'show-inheritance': 1,
    'members': True,  # 'var1, var2',
    'member-order': 'bysource',
    # 'inherited-members': False,
    # 'special-members': '__call__',
    'undoc-members': True,
    # 'exclude-members': '__weakref__',
    # 'autosummary': True,
    'inherit_docstrings': True
}
numpydoc_show_class_members=True
autoclass_content = 'both'
#autosummary_generate = True

# needed for version 1.8.5 (python 2.7)
autodoc_default_flags = [ 'members', 'show-inheritance']
autodoc_member_order = 'bysource' #'groupwise'
autodoc_inherit_docstrings = True

#source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = pkg.__name__.capitalize()
copyright = pkg.__author__
author = pkg.__email__

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pkg.__version__
# The full version, including alpha/beta/rc tags.
release = pkg.__version__ + ' [' + pkg.__dev_status__ + ']'
# today as date of release
today = pkg.__date__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# A boolean that decides whether module names are prepended to all object names.
add_module_names = True

# Read rst_prolog and rst_epilog from file
rst_prolog, rst_epilog = '', ''

rst_prolog_file = '_static' + os.sep + 'rst_prolog.rst'
if os.path.exists(rst_prolog_file):
    f = open(rst_prolog_file, 'r')
    rst_prolog += os.linesep + f.read()
    f.close()

rst_epilog_file = '_static' + os.sep + 'rst_epilog.rst'
if os.path.exists(rst_epilog_file):
    f = open(rst_epilog_file, 'r')
    rst_epilog += os.linesep + f.read()
    f.close()

# extend rst_prolog with pkg items
_replacements = replacements_from_pkg(replacements, pkg)
rst_prolog += os.linesep + replacements_str(_replacements)

# print(rst_prolog)
# print(rst_epilog)


# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_logo = 'logo.png'
# html_theme_options = {}
# html_static_path = ['_static']


# -- Options for LaTeX output ---------------------------------------------

latex_logo = 'logo.png'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(
    master_doc,
    pkg.__name__ + '.tex',
    pkg.__name__.capitalize() + ' Documentation',
    pkg.__author__,
    'manual'
),]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

man_pages = [(
    master_doc,
    pkg.__name__,
    pkg.__name__.capitalize() + ' Documentation',
    [pkg.__author__],
    1)
]
