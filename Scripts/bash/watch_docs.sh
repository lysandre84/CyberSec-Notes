#!/usr/bin/env bash
# Surveillance des fichiers docs pour recompiler
while inotifywait -e modify -r Docs; do
  mkdocs build
done
