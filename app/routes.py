import os
from flask import render_template, Blueprint, url_for, current_app
from app.models import Character, HSRGame8

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

@bp.route('/genshin', methods=["GET"])
def genshin():
    genshinchars = Character.query.filter_by(game="Genshin").all()
    return render_template("hsr.html", genshinchars=genshinchars)

@bp.route("/hsr/character/<slug>")
def character_detail(slug):
    character = Character.query.filter_by(slug=slug).first_or_404()
     # Look for fort image with .jpg or .png
    base_path = os.path.join(current_app.static_folder, 'images', 'HSR', 'Characters', character.slug)
    fort_filename = None
    for ext in ['.jpg', '.png']:
        potential_path = os.path.join(base_path, f"fort{ext}")
        if os.path.exists(potential_path):
            fort_filename = f"images/HSR/Characters/{character.slug}/fort{ext}"
            break
    game8 = HSRGame8.query.filter_by(slug=slug).first_or_404()
    return render_template("hsrbuild.html", character=character, title=character.name, fort_image=fort_filename, game8=game8)