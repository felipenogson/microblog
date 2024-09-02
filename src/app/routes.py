from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from app import db
from app.models import User
from flask_login import login_required
from urllib.parse import urlsplit


@app.route('/')
@app.route('/index')
@login_required
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
  return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next')
    if not next_page or urlsplit(next_page).netloc != '':
      next_page = url_for('index')
    return redirect(next_page)
    flash(f'Login requested for user { form.username.data }, {form.remember_me.data}')
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))
  
