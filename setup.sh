#!/bin/bash
# setup.sh

echo "installing nltk..."
pip install nltk

echo "Downloading and linking spacy..."
pip install spacy
# Install the exact model version that matches your spacy version
python -m spacy download en_core_web_sm
# The 'download' command automatically runs 'link'
