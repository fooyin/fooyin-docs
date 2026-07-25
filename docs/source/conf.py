# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'fooyin'
copyright = '2024, Luke Taylor'
author = 'ludouzi'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = 'logo.svg'
html_favicon = 'favicon.ico'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'collapse_navigation': False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
