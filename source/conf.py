# Configuration file for the Sphinx documentation builder.

### Project Information ###

project = 'nnsight'
copyright = '2025, Jaden Fiotto-Kaufman'
author = 'Jaden Fiotto-Kaufman'
release = '0.5.0'

### Extensions ###

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "nbsphinx"
]

templates_path = ['_templates']
exclude_patterns = []

### HTML Options ###

html_theme = 'furo'
html_static_path = ['_static']
html_title = "NNsight"
