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
import pytz


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
    """
    The order of priority should be

    Locale from URL parameters
    Locale from user settings
    Locale from request header
    Default locale
    """
    if request.args.get("locale") is not None:
        return request.args["locale"]
    if g.user \
        and g.user.get("locale") is not None \
            and g.user.get("locale") in app.config.get("LANGUAGES"):
        return g.user["locale"]
    return request.accept_languages.best_match(app.config.get("LANGUAGES"))


@babel.timezoneselector
def get_timezone() -> str:
    """
    The order of priority should be

    Find `timezone` parameter in URL parameters
    Find time zone from user settings
    Default to UTC
    """
    try:
        timezone = request.args.get("timezone") \
            or g.user.get("timezone") if g.user else None
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config.get("BABEL_DEFAULT_TIMEZONE")


def get_user() -> dict | None:
    """Returns a user dictionary or None"""
    user_id = request.args.get("login_as", "-1")
    return users.get(int(user_id)) if user_id.isdigit() else None


@app.before_request
def before_request():
    g.user = get_user()


@app.route("/")
def root() -> Response:
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
