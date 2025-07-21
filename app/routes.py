from flask import render_template
from app import app

#Routes

#HOME PAGE
@app.route ('/')
def home():
    return render_template('home.html', title='Account')