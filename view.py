# Model - db
# View - view
# Controller - reqeust and redirect
from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'Ivan'
    return render_template('index.html', n=name)
# {'/': 'view.index',
# '/blog': 'index'}