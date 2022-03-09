# Third party imports
from flask_restx import Api

# Local imports
from apis.average_clicks_by_country import api as ns_average_clicks_by_country

# Instantiate Api object
api = Api(
    title="bitly",
    version="1.0",
    description="Bitly technical assessment",
)

# Add flask_restx namespaces to API
api.add_namespace(ns_average_clicks_by_country)
