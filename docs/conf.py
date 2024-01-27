# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from __future__ import annotations

import os
import re
import sys
from dataclasses import asdict

from sphinxawesome_theme import ThemeOptions
from sphinxawesome_theme.postprocess import Icons

sys.path.insert(0, os.path.abspath("../"))
version = ""
copyright = ""
author = ""
project = ""


with open("../rankade/__init__.py") as f:
    read = f.read()
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', read, re.MULTILINE).group(1)
    copyright = re.search(r'^__copyright__\s*=\s*[\'"]([^\'"]*)[\'"]', read, re.MULTILINE).group(1)
    author = re.search(r'^__author__ \s*=\s*[\'"]([^\'"]*)[\'"]', read, re.MULTILINE).group(1)
    project = re.search(r'^__title__ \s*=\s*[\'"]([^\'"]*)[\'"]', read, re.MULTILINE).group(1)
release = version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# The master toctree document.
root_doc = "index"


extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    # "sphinx.ext.autodoc",
    "sphinx_sitemap",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "autodoc2",
    "sphinx_autodoc_typehints",
    "enum_tools.autoenum",
    "myst_parser",
    "sphinxawesome_theme.highlighting",
    "sphinxcontrib.spelling",
]
source_suffix = [".rst", ".md"]

templates_path = ["_templates"]
pygments_style = "sphinx"
nitpicky = True
nitpick_ignore = [
    ("py:class", "rankade.models.Game"),
    ("py:class", "rankade.models.Games"),
    ("py:class", "rankade.models.Match"),
    ("py:class", "rankade.models.Matches"),
    ("py:class", "rankade.models.Player"),
    ("py:class", "rankade.models.Players"),
    ("py:class", "rankade.models.Quota"),
    ("py:class", "rankade.models.Subset"),
    ("py:class", "rankade.models.Subsets"),
    ("py:class", "rankade.models.Ranking"),
    ("py:class", "rankade.models.Rankings"),
    ("py:class", "rankade.models.NewMatch"),
    ("py:class", "rankade.models.NewMatchResponse"),
    ("py:class", "rankade.models.MatchStatus"),
    ("py:class", "rankade.api.Api.HEADERS"),
    ("py:class", "rankade.api.Api.JSON"),
    ("py:class", "rankade.api.Api.PARAMS"),
    ("py:class", "rankade.models.Base.T"),
]
add_module_names = False
# -- Options for Python domain -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-python-domain
python_display_short_literal_types = True
python_use_unqualified_type_names = True

# -- Options for sphinx.ext.intersphinx output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable", None),
    "pyjwt": ("https://pyjwt.readthedocs.io/en/stable", None),
}
# -- Options for sphinxcontrib.spelling output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html
coverage_show_missing_items = True
# -- Options for sphinxcontrib.spelling output -------------------------------------------------
# https://sphinxcontrib-spelling.readthedocs.io/en/latest/customize.html
spelling_lang = "en_GB"
tokenizer_lang = "en_GB"
spelling_warning = True

# -- Options for sphinx.ext.napoleon output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_numpy_docstring = True
napoleon_use_rtype = True

# -- Options for autodoc2 output -------------------------------------------------
# https://sphinx-autodoc2.readthedocs.io/en/latest/config.html
autodoc2_packages = [
    "../rankade",
]

autodoc2_docstring_parser_regexes = [
    # this will render all docstrings as Markdown
    (r".*", "myst"),
]
autodoc2_output_dir = "api"
autodoc2_hidden_objects = ["inherited"]

# -- Options for MyST output -------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html
myst_number_code_blocks = ["python"]
myst_enable_extensions = [
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "replacements",
    "linkify",
    "strikethrough",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]

myst_linkify_fuzzy_links = False

# -- Options for sphinx-sitemap -------------------------------------------------
# https://sphinx-sitemap.readthedocs.io/en/latest/index.html
html_baseurl = "https://calumcrawford.com/rankadepy"


# -- Options for HTML output & Theme -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://sphinxawesome.xyz/how-to/configure/
html_title = "Rankade.py"
html_theme = "sphinxawesome_theme"
html_static_path = ["static"]
html_sidebars: dict[str, list[str]] = {
    "about": ["sidebar_main_nav_links.html"],
    "changelog/*": ["sidebar_main_nav_links.html"],
}

html_permalinks_icon = Icons.permalinks_icon
html_static_path = ["_static"]

theme_options = ThemeOptions(
    awesome_external_links=True,
    awesome_headerlinks=True,
    breadcrumbs_separator="/",
    extra_header_link_icons={
        "Github": {
            "link": "https://github.com/14zombies/Rankade.py/",
            "icon": (
                '<svg height="26px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 45 44" '
                'fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" clip-rule="evenodd" '
                'd="M22.477.927C10.485.927.76 10.65.76 22.647c0 9.596 6.223 17.736 '
                "14.853 20.608 1.087.2 1.483-.47 1.483-1.047 "
                "0-.516-.019-1.881-.03-3.693-6.04 "
                "1.312-7.315-2.912-7.315-2.912-.988-2.51-2.412-3.178-2.412-3.178-1.972-1.346.149-1.32.149-1.32 "
                "2.18.154 3.327 2.24 3.327 2.24 1.937 3.318 5.084 2.36 6.321 "
                "1.803.197-1.403.759-2.36 "
                "1.379-2.903-4.823-.548-9.894-2.412-9.894-10.734 "
                "0-2.37.847-4.31 2.236-5.828-.224-.55-.969-2.759.214-5.748 0 0 "
                "1.822-.584 5.972 2.226 "
                "1.732-.482 3.59-.722 5.437-.732 1.845.01 3.703.25 5.437.732 "
                "4.147-2.81 5.967-2.226 "
                "5.967-2.226 1.185 2.99.44 5.198.217 5.748 1.392 1.517 2.232 3.457 "
                "2.232 5.828 0 "
                "8.344-5.078 10.18-9.916 10.717.779.67 1.474 1.996 1.474 4.021 0 "
                "2.904-.027 5.247-.027 "
                "5.96 0 .58.392 1.256 1.493 1.044C37.981 40.375 44.2 32.24 44.2 "
                '22.647c0-11.996-9.726-21.72-21.722-21.72" '
                'fill="currentColor"/></svg>'
            ),
        }
    },
    main_nav_links={"Docs": "./index", "Changelog": "./changelog/index"},
    show_prev_next=False,
    show_breadcrumbs=True,
)

html_theme_options = asdict(theme_options)
