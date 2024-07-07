#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask import (
    Flask,
    render_template,
    request,
    Response,
    Request
)
from flask_babel import Babel


class Config:
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Request:
    if request.args.get("locale") is not None:
        return request.args["locale"]
    return request.accept_languages.best_match(app.config.get("LANGUAGES"))


@app.route("/")
def root() -> Response:
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
