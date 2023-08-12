.PHONY: all

all:
	docker build --tag short-url-service:backend-latest --file server/python3/Dockerfile server/python3
	docker build --tag short-url-service:frontend-latest --file frontend/Dockerfile frontend/
