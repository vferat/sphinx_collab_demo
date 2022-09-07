# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'demo'
copyright = '2022, Victor Férat'
author = 'Victor Férat'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates', 'spelling.txt']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# Extensions
extensions = ['myst_parser',
              'sphinxcontrib.bibtex',
              'sphinxcontrib.spelling',
              'sphinx_tabs.tabs',
              'sphinx_togglebutton']

# myst_parser
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
suppress_warnings = ["myst.footnote"]
myst_footnote_transition = False

# bibtex
bibtex_bibfiles = ['./bibliography.bib']

# Spelling
spelling_word_list_filename = ['spelling.txt']
spelling_show_suggestions = True
spelling_show_suggestions  = 5
