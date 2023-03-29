from pathlib import Path

html_theme = "pydata_sphinx_theme"
html_theme_options = {
  "navbar_start": ["navbar-logo", "version"],
  "navbar_center": ["header"],
}

html_logo = "https://brainglobe.info/images/brainglobe.png"
templates_path = [str(Path(__file__).parent / '_templates')]
