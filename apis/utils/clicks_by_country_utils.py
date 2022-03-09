# Third party imports
import requests

# Get data from API request
def get_clicks_by_country(bitlink: str, headers: dict) -> dict:
    """Provides the number of user clicks, broken down by country, for a provided Bitlink

    Args:
        bitlink: a link in the Bitly ecosystem
        headers: request headers with bearer token authorization

    Returns:
        Data about an individual bitlink
    """
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/countries"
    response = requests.get(url, headers=headers)
    return response.json()
