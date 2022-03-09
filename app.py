# Third party imports
from flask import Flask

# Local imports
from apis import api

# Instantiate Flask app
app = Flask(__name__)
api.init_app(app=app)
