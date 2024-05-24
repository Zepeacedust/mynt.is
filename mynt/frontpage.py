from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

bp = Blueprint("frontpage", __name__)

@bp.route("/")
def index():
    """Show front page"""
    return "FRONTPAGE"