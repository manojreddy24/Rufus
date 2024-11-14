# src/utils.py

import requests

def safe_request(url, retries=3):
    """
    Helper function to make a safe request with retries.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            continue
    return None
