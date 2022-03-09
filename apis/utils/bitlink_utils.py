# Third party imports
import requests

# Get data from API request
def get_bitlinks_by_group(group: str, page: int, headers: dict) -> dict:
    """Return a list of 50 bitlinks belonging to a group

    Args:
        group: An organization of users
        page: Set of 50 results accounting for pagination
        headers: Request headers with bearer token authorization

    Returns:
        Data about bitlinks belonging to a provided group
    """
    url = f"https://api-ssl.bitly.com/v4/groups/{group}/bitlinks?page={page}"
    response = requests.get(url, headers=headers)
    return response.json()
