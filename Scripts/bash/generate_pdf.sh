#!/usr/bin/env bash
# Génère PDF à partir des docs MkDocs
mkdocs build --clean
wkhtmltopdf site/index.html site/CyberSec-Notes.pdf
