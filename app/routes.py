from flask import render_template, Blueprint, url_for
from app.models import Character

#Routes
bp = Blueprint("routes", __name__)


#HOME PAGE
@bp.route ('/')
def home():
    return render_template('home.html', title='Home')

@bp.route('/hsr', methods=["GET"])
def hsr():
    hsrchars = Character.query.filter_by(game="HSR").all()
    return render_template("hsr.html", hsrchars=hsrchars)

@bp.route("/character/<slug>")
def character_detail(slug):
    character = Character.query.filter_by(slug=slug).first_or_404()
    return render_template("hsrbuild.html", character=character, title=character.name)