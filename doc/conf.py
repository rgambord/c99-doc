# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'C Language Standards 9899:TC3 (C99)'
author = 'Ryan Gambord'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_show_sphinx = False
html_show_copyright = False
html_show_sourcelink = False

html_theme_options = {
        'style_external_links': True,
        'prev_next_buttons_location': 'both',
        'navigation_depth': -1,
        'navigation_with_keys': True,
        }

html_css_files = [
        'css/brand.css',
        ]
highlight_language = 'c'
primary_domain = 'c'
rst_prolog = """
.. role:: c(code)
   :language: c
.. role:: asm(code)
   :language: asm
.. role:: make(code)
   :language: make
.. role:: bash(code)
   :language: bash
.. role:: console(code)
   :language: console

.. default-role:: c
"""

extensions = ['sphinx.ext.imgmath']

imgmath_image_format = 'svg'


