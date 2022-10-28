# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Microstates HUB'
copyright = '2022, EEG Microstates Community'
author = 'EEG Microstates Community'
github_user = "EEG-microstates-Community"
github_project = 'Microstates_HUB'
gh_url = f"https://github.com/{github_user}/{github_project}/"
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates', 'spelling.txt']
exclude_patterns = []

numfig = True

html_title = "Microstates HUB"
html_logo = "path/to/logo.png"
html_favicon = "path/to/favicon.ico"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    "repository_url":  gh_url,
    "path_to_docs": "source/",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "repository_branch": "main",
    "use_fullscreen_button": False,
    "launch_buttons": {
        #"thebe": True,
        "binderhub_url": "https://mybinder.org/"
    },
    
}

# Extensions
extensions = ['myst_parser',
              'sphinxcontrib.bibtex',
              'sphinxcontrib.spelling',
              'sphinx_tabs.tabs',
              'sphinx_togglebutton',
              "sphinx_thebe",
              "sphinx_issues",]

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

# sphinx-issues
issues_github_path = gh_url.split("http://github.com/")[-1]
