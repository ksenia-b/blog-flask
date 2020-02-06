# Model - db
# View - view
# Controller - reqeust and redirect
from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'Ivan'
    return render_template('index.html', n=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
