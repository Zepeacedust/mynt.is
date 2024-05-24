from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

bp = Blueprint("news", __name__)

@bp.route("/news")
def index():
    """Show all the posts, most recent first."""
    return "NEWS"