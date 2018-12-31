from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'user_name': 'Isaac'}
    posts = [
        {
            'author': {'user_name': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'user_name': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
