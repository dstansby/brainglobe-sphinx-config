from pathlib import Path

html_theme = "pydata_sphinx_theme"
html_theme_options = {
  "external_links": [
      {"name": "About", "url": "https://brainglobe.info/about"},
  ],
  "navbar_start": ["navbar-logo", "version"],
}

html_logo = "https://brainglobe.info/images/brainglobe.png"
templates_path = [str(Path(__file__).parent / '_templates')]
