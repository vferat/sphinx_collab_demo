# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'demo'
copyright = '2022, Victor Férat'
author = 'Victor Férat'
github_user = "vferat"
github_project = 'sphinx_collab_demo'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    "repository_url": github_user + "/" + github_project,
    "path_to_docs": "source/",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "repository_branch": "main",
    #"launch_buttons": True, # Add binder to jupyter notebook pages
}

# Extensions
extensions = ['myst_parser',
              'sphinxcontrib.bibtex',
              'sphinxcontrib.spelling']

# myst_parser
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# bibtex
bibtex_bibfiles = ['./bibliography.bib']

# Spelling
spelling_word_list_filename = ['spelling.txt']
spelling_show_suggestions = True
spelling_show_suggestions  = 5
