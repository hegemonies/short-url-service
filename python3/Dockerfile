FROM python:3.11.1-slim-buster

WORKDIR /app

COPY ./ /app

# Install poetry
RUN apt update && apt install curl -y
RUN curl -sSL https://install.python-poetry.org | python3 -

# Install project
RUN $HOME/.local/bin/poetry install

CMD $HOME/.local/bin/poetry run flask run --host=0.0.0.0
