# Bitly Technical Assessment
By Matthew Young

## Design Decisions
Most of what I do right now is writing Python code using the Flask framework, so I defaulted to those technologies because of the 90 minute time. Admittedly, I did take closer to 2 hours when completing this assessment.

I used the flask_restx module because it's what I use at my current job, and it makes endpoint creation easy and painless after some initial setup.

I included a `utils/` folder to abstract away the API calls. I figure these calls might also be used in other functionality in the future.

I wrote docstrings for all my functions and included plenty of explanatory comments because I know how much more maintainable it makes the code.

I utilized a Dockerfile and Makefile to make setup a little easier.

## Dependencies
1. [Docker](https://www.docker.com/products/docker-desktop) (Click to install)

## How to Get Started
1. Clone and navigate to project folder from command line
2. Run `make start_project`

The Flask application will run on port 5000 of your localhost by default. You can access a Swagger page on http://localhost:5000.

## Endpoint
The endpoint below will require a Bitly access_token in the format of "Bearer {access_token}"

* /average_clicks_by_country
    - `curl -H 'Authorization: {TOKEN}' -X GET http://localhost:5000/average_clicks_by_country`
