#!/usr/bin/env python3
"""
Mocking login
"""
from flask import (
    Flask,
    render_template,
    request,
    g,
    Response
)
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    if request.args.get("locale") is not None:
        return request.args["locale"]
    return request.accept_languages.best_match(app.config.get("LANGUAGES"))


def get_user() -> dict | None:
    """Returns a user dictionary or None"""
    user_id = request.args.get("login_as", "-1")
    return users.get(int(user_id)) if user_id.isdigit() else None


@app.before_request
def before_request():
    g.user = get_user()


@app.route("/")
def root() -> Response:
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
