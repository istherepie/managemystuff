# -- coding: utf-8 --

from os import getenv
from flask import Flask, jsonify, request

import database as db


app = Flask(__name__)


# Server settings
expose = getenv("EXPOSE_SERVER", False)

if expose:
    host = "0.0.0.0.0"
else:
    host = "127.0.0.1"

port = getenv("SERVER_PORT", 8080)


@app.route("/", methods=["GET"])
def index():
    """
    Say hello to the world

    :return: Hello (Type: json)
    """

    greeting = {
        "status": 200,
        "message": "Hello World"
    }

    return jsonify(greeting), 200


@app.route("/all", methods=["GET"])
def all_stuff():
    """
    Get all the stuff

    :return: Stuff (Type: list)
    """

    all_the_stuff = db.get_all_the_stuff()

    return jsonify(all_the_stuff), 200


@app.route("/new", methods=["POST"])
def new_stuff():
    """
    Create new stuff

    :return: Stuff (Type: list)
    """

    new_stuff = request.get_json()

    if not new_stuff:
        raise RuntimeError("I simply can't go on")

    # Do something with the new stuff
    # Store it somewhere maybe ?

    return_uuid = db.store_it("stuff")

    confirmation = {
        "stored": True,
        "uuid": return_uuid,
        "data": new_stuff
    }

    return jsonify(confirmation), 201


if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)
