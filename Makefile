make start_project: ## Build and run project in a docker container
	docker build -t bitly .
	docker run -p 5000:5000 --rm -it bitly

make test: ## Run tests
	python -m pytest --disable-warnings
