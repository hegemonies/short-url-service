FROM python:3.9.9-slim-buster

WORKDIR /app

COPY ./ /app

# Install poetry
RUN apt update && \
        apt install curl -y && \
        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Install project
RUN $HOME/.poetry/bin/poetry install

CMD $HOME/.poetry/bin/poetry run flask run --host=0.0.0.0
