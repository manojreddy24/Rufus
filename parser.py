# src/parser.py

import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def parse_instructions(instructions):
    """
    Parse user instructions to extract keywords for focused web scraping.
    """
    doc = nlp(instructions)
    keywords = [token.lemma_ for token in doc if token.pos_ in {'NOUN', 'PROPN'}]
    return keywords
