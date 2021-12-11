from flask import Flask, request, redirect
from flask_caching import Cache
import hashlib
from dotenv import dotenv_values
import redis

config = dotenv_values(".env")

redis_client = redis.Redis(host=config["REDIS_HOST"], port=config["REDIS_PORT"], db=0)

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

base_url = config["BASE_URL"]

hash_encoder = hashlib.md5()

def generate_hash(url: str) -> str:
    hash_encoder.update(bytes(url, 'utf-8'))
    return hash_encoder.hexdigest()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/generate", methods=["GET"])
def generate_url():
    origin_url = str(request.query_string).split("=")[1][:-1]
    hash_url = generate_hash(origin_url)
    redis_client.set(hash_url, origin_url)
    return "http://" + base_url + "/go?url=" + hash_url

@app.route("/go", methods=["GET"])
def go():
    hash_url = str(request.query_string).split("=")[1][:-1]
    origin_url = redis_client.get(hash_url).decode("utf-8")
    return redirect(origin_url, code=302)
