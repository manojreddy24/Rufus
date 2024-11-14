# src/crawling/dynamic_content.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup


def load_dynamic_content(url):
    """
    Use Selenium to load dynamic content from a webpage.
    """
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service('path/to/chromedriver'), options=options)
    driver.get(url)
    time.sleep(3)  # Adjust for page load time

    page_source = driver.page_source
    driver.quit()
    return BeautifulSoup(page_source, "html.parser")
