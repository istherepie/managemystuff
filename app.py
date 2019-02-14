# -- coding: utf-8 --

from os import getenv
from flask import Flask, jsonify, request, g

from datastore import RethinkdbInterface

def startup():
    return Flask(__name__)

app = startup()

db = RethinkdbInterface()


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
        "message": "Hello World"
    }

    return jsonify(greeting), 200


@app.route("/all", methods=["GET"])
def all_stuff():
    """
    Get all the stuff

    :return: Stuff (Type: list)
    """

    all_the_stuff = db.all("stuff")

    return jsonify(all_the_stuff), 200


@app.route("/get/<uuid:stuff_uuid>", methods=["GET"])
def get_stuff(stuff_uuid):
    """
    Get stuff by uuid

    :return: Stuff (Type: dict/json)
    """

    get_stuff = db.get("stuff", stuff_uuid)

    response = {
       "stuff": get_stuff
    }

    return jsonify(response), 200


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

    return_uuid = db.insert("stuff", new_stuff)

    return jsonify(return_uuid), 201


@app.route("/delete/<uuid:stuff_uuid>", methods=["DELETE"])
def delete_stuff(stuff_uuid):
    """
    Delete some stuff

    :return: Stuff (Type: list)
    """

    status = db.delete("stuff", stuff_uuid)

    return jsonify(status), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)