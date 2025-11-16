#!/bin/bash
# setup.sh

echo "Downloading and linking spacy model..."
# Install the exact model version that matches your spacy version
python -m spacy download en_core_web_sm
# The 'download' command automatically runs 'link'