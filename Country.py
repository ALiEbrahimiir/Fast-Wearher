import requests
from bs4 import BeautifulSoup


def country():
    # Define the URL
    url = 'https://weather.town/'

    # Fetch the HTML content from the URL
    url = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(url.text, 'html.parser')

    # Find all <span> elements that contain the location names
    # Update the class names based on the actual HTML structure you inspect
    location_spans = soup.find_all("span", class_="country-link-text")

    # Extract and print the location names
    locations = [span.get_text(strip=True) for span in location_spans]

    return locations
