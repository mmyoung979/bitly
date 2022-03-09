# Python imports
from math import ceil

# Third party import
from flask import request
from flask_restx import Namespace, Resource

# Local imports
from apis.utils.bitlink_utils import get_bitlinks_by_group
from apis.utils.clicks_by_country_utils import get_clicks_by_country
from apis.utils.user_utils import get_user_group

# Global variables
DESCRIPTION = "Provides average number of clicks of all links per country for a group"
api = Namespace("average_clicks_by_country", description=DESCRIPTION)


@api.route("/", strict_slashes=False)
class AverageClicksByCountry(Resource):
    @api.doc(DESCRIPTION, description=DESCRIPTION)
    def get(self) -> dict:
        # Get Authorization header
        access_token = request.headers.get("Authorization")
        headers = {"Authorization": access_token}

        # Get user's group from access token
        group = get_user_group(access_token, headers)

        # Get bitlinks associated with group
        page = 1
        bitlinks = get_bitlinks_by_group(group, page, headers)
        size = bitlinks["pagination"]["size"]
        num_of_pages = ceil(bitlinks["pagination"]["total"] / size)

        # Data to be used throughout while loop below
        days = 30
        total_clicks = {}

        # Iterate through pages of links
        while page <= num_of_pages:

            # Don't send a duplicate request for first page
            if page != 1:
                bitlinks = get_bitlinks_by_group(group, page, headers)

            # Get total number of clicks per link
            for bitlink in bitlinks["links"]:

                # Ignore http:// and https://
                link = bitlink["link"].split("://")[1]

                # Retrieve and parse API data
                clicks_by_country = get_clicks_by_country(link, headers)
                metrics = clicks_by_country["metrics"]

                # Get total number of clicks per country per link
                for metric in metrics:
                    country_name = metric["value"]

                    # If country hasn't been seen yet, add to dict
                    if not total_clicks.get(country_name):
                        total_clicks[country_name] = 0

                    # Add clicks to total for country across all links
                    total_clicks[country_name] += metric["clicks"]

            # Paginate as necessary
            page += 1

        # Find averages
        for country in total_clicks.keys():
            total_clicks[country] = round(total_clicks[country] / days, 2)

        return {
            "group": group,
            "average_clicks_per_day": total_clicks,
        }
