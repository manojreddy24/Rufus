# src/extraction/scraper.py

from bs4 import BeautifulSoup

def selective_scrape(soup, keywords):
    """
    Filter and extract content from a page that matches given keywords.
    """
    extracted_data = []
    for keyword in keywords:
        sections = soup.find_all(string=lambda text: text and keyword in text.lower())
        for section in sections:
            parent = section.find_parent()
            extracted_data.append(parent.get_text(strip=True))
    return extracted_data
