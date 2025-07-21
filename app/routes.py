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
    hsrchar_names = [char.name for char in Character.query.filter_by(game="HSR").all()]
    return render_template("hsr.html", names=hsrchar_names)