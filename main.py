# src/main.py

from crawler import crawl

def main():
    # Input: Website link and user prompt
    url = input("Enter the website URL: ")
    instructions = input("Enter your instructions (e.g., 'Find product information and FAQs'): ")

    # Perform crawling and data extraction
    extracted_html = crawl(url, instructions)

    # Display or save the extracted HTML content
    if extracted_html:
        print("\nExtracted HTML Content:")
        for section in extracted_html:
            print(section)
    else:
        print("No relevant content found or failed to retrieve the page.")

if __name__ == "__main__":
    main()
