#!/usr/bin/env python3
import json, sys
# Lit un glossaire et génère un jeu de flashcards JSON
glossary_file = 'Docs/Glossary.md'
cards = []
with open(glossary_file) as f:
    lines = f.readlines()
for line in lines:
    if line.startswith('- **'):
        term, desc = line[3:].split('**: ')
        desc = desc.strip()
        term = term.strip('* ')
        cards.append({'term': term, 'definition': desc})
print(json.dumps(cards, indent=2))
