# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CDS-UTE-Documentation-Project'
copyright = '2025, Tran Huu Hieu'
author = 'Tran Huu Hieu'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,   # hiện tất cả menu
    'body_max_width': '90%',  # docs full rộng như Bosch
}

html_static_path = ['_static']
html_favicon = "_static/ute_ai_lab.jpg"

# nếu bạn có logo riêng
# html_logo = "_static/logo.png"

# CSS custom thêm
html_css_files = ['custom.css']
