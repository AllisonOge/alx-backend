#!/usr/bin/env python3
"""
Using babel flask extension
"""
from flask import Flask, render_template, Response
from flask_babel import Babel


class Config:
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def root() -> Response:
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
