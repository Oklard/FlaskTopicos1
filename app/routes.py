from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Paulo'}
    posts = [
        {
            'author': {'username': 'José'},
            'body': 'Esse é um post de teste!'
        },
        {
            'author': {'username': 'Maria'},
            'body': 'Esse é outro post de teste!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)