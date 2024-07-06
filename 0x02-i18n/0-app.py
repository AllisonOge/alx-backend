#!/usr/bin/env python3
"""
simple flask app
"""
from flask import Flask, render_template, Response


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def root() -> Response:
    """render index page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
