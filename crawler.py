# src/crawler.py

from bs4 import BeautifulSoup
import requests
from parser import parse_instructions
from utils import safe_request

def find_relevant_sections(soup, keywords):
    """
    Extract HTML sections that contain any of the specified keywords.
    """
    relevant_sections = []
    for keyword in keywords:
        # Search for text that contains the keyword
        sections = soup.find_all(string=lambda text: text and keyword.lower() in text.lower())
        for section in sections:
            parent = section.find_parent()  # Get the enclosing HTML element
            relevant_sections.append(str(parent))
    return relevant_sections

def crawl(base_url, instructions):
    """
    Crawl the base URL and extract relevant HTML based on instructions.
    """
    # Parse instructions to get keywords
    keywords = parse_instructions(instructions)
    print(f"Keywords extracted: {keywords}")

    # Request the page
    response = safe_request(base_url)
    if not response:
        print("Failed to retrieve the page.")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and return relevant HTML sections
    return find_relevant_sections(soup, keywords)
