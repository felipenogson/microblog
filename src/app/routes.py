from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username':'felipon'}
  posts = [
    {
      'author' : { 'username' : 'Jhon'},
      'body' : 'Beautiful day in el Chuco'
    },

    {
      'author' : { 'username' : 'Susan'},
      'body' : 'The Terminator 2 movie is so great!!'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)
