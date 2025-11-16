#!/bin/bash
# setup.sh

echo "installing nltk..."
pip install nltk

echo "installing scikit-learn..."
pip install scikit-learn==1.6.1

echo "Downloading and linking spacy..."
pip install spacy

echo "Downloading en_core_web_sm..."
python -m spacy download en_core_web_sm
# The 'download' command automatically runs 'link'

echo "Installing scipy..."
pip install scipy

echo "Getting all versions..."
pip freeze
