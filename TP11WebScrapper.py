import requests
from bs4 import BeautifulSoup
import json

def extract_data(url):
    """Extracts useful data from a website."""

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error HTTP statuses
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract basic information
        site_name = soup.title.string
        num_hyperlinks = len(soup.find_all('a'))
        # ... extract more hyperlinks data if needed (e.g., hrefs, text)

        # Extract additional information
        meta_description = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else None
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})['content'] if soup.find('meta', attrs={'name': 'keywords'}) else None
        header_tags = [h.text for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        # ... extract more information as needed (e.g., images, scripts, stylesheets)

        data = {
            'site_name': site_name,
            'num_hyperlinks': num_hyperlinks,
            'meta_description': meta_description,
            'meta_keywords': meta_keywords,
            'header_tags': header_tags
        }

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_data_to_file(data, filename):
    """Saves extracted data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage write the name of the website. Be Aware and Adhere to the websites robots.txt file!
url = "https://youtube.com/"
data = extract_data(url)
if data:
    save_data_to_file(data, 'Crawler_Data.txt')
