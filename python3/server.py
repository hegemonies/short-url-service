from datetime import timedelta
from flask import Flask, request, redirect
from flask_caching import Cache
import hashlib
from dotenv import dotenv_values
import redis
import os
import urllib
from urllib.parse import urlparse

config = dotenv_values(".env")

redis_client = redis.Redis(host=os.environ["REDIS_HOST"], port=int(os.environ["REDIS_PORT"]), db=0)
if redis_client.ping() is not True:
    exit(1)

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

base_url = os.environ["BASE_URL"]

hash_encoder = hashlib.md5()


def generate_hash(url: str) -> str:
    hash_encoder.update(bytes(url, 'utf-8'))
    return hash_encoder.hexdigest()


def get_address_from_url(query_string: str) -> str:
    return urllib.parse.unquote(query_string).split("=")[1][:-1]


@app.route("/generate", methods=["GET"])
def generate_url():
    origin_url = get_address_from_url(request.query_string)
    print(f"origin_url = {origin_url}")
    hash_url = generate_hash(origin_url)
    key = hash_url
    redis_client.set(key, origin_url)
    redis_client.expire(key, timedelta(minutes=1))
    return base_url + "/go?url=" + hash_url


@app.route("/go", methods=["GET"])
def go():
    hash_url = str(request.query_string).split("=")[1][:-1]
    origin_url = redis_client.get(hash_url).decode("utf-8")
    if origin_url[:4] != "http":
        origin_url += "https://"
    return redirect(origin_url, code=302)
