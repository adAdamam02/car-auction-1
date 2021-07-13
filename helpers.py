from functools import wraps
from flask import redirect, render_template, request, session
import scrapy

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def usd(value):
    """Format value as USD."""
    return f"${int(value):,}"


def time_format(value):
    days = int(value)

    return f"{days} Days" if days > 0 else f"{int((value - days) * 24)} Hours"