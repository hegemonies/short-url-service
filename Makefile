.PHONY: build-all build-push-all build-backend build-frontend push-backend push-frontend

build-all: build-backend build-frontend

build-push-all: build-backend build-frontend push-backend push-frontend

build-backend:
	docker build --tag hegemonies/short-url-service:backend-latest --file server/python3/Dockerfile server/python3

build-frontend:
	docker build --tag hegemonies/short-url-service:frontend-latest --file frontend/Dockerfile frontend/

push-backend:
	docker push hegemonies/short-url-service:backend-latest

push-frontend:
	docker push hegemonies/short-url-service:frontend-latest
