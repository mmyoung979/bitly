# Third party imports
import requests


def get_user_data(access_token: str, headers: dict) -> dict:
    """Provides user information including the user's default group

    Args:
        access_token: Bearer token from Bitly
        headers: request headers with bearer token authorization

    Returns:
        Data about user associated with access_token
    """
    # Get data from API request
    url = "https://api-ssl.bitly.com/v4/user"
    response = requests.get(url, headers=headers)
    return response.json()


def get_user_group(access_token: str, headers: dict) -> str:
    """Parse default group from user data

    Args:
        access_token: Bearer token from Bitly
        headers: request headers with bearer token authorization

    Returns:
        Default user group
    """
    return get_user_data(access_token, headers)["default_group_guid"]
