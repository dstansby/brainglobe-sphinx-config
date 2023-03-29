from pathlib import Path
import json

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "navbar_start": ["navbar-logo", "version"],
    "navbar_center": ["header"],
}

html_logo = "https://brainglobe.info/images/brainglobe.png"
_templates_Path = Path(__file__).parent / "_templates"
templates_path = [str(_templates_Path)]

header_links = json.load(open(_templates_Path / "header_links.json"))

html_context = {"header_links": header_links}
