# src/utils/helpers.py

import requests

def safe_request(url, retries=3):
    """
    Helper function to make a safe request with retries.
    """
    for _ in range(retries):
        try:
            return requests.get(url)
        except requests.RequestException as e:
            continue
    return None
