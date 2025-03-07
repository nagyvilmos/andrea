# Copyright (c) Daniella Norman-Walker. All rights reserved.
import os.path
from config import settings
from flask import Flask, send_from_directory, json
from server.controller import add_controllers
from server.dbClient import innitialise_database

innitialise_database(settings)
app = Flask(__name__)

"""
Main routes path.
All routing is client side, and so we just serve up the app.
"""
@app.route("/")
@app.route("/<path:path>")
def home(path = None):
    if path is not None:
        filename = f'client/dist/{path}'
        print(filename)
        if os.path.isfile(filename):
            return send_from_directory('client/dist', path)

    return send_from_directory('client/dist', 'index.html')

"""
Path for all the static files (compiled JS/CSS, etc.)
"""
@app.route("/resource/<path:path>")
def content(path):
    return send_from_directory('client/dist', path)


add_controllers(app)

if __name__ == "__main__":
    app.run(debug=True, port=61975)
