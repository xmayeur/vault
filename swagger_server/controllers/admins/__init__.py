# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user

from swagger_server.form import LoginForm
from swagger_server.models import User

adm = Blueprint('admins', __name__)


@adm.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admins.do_index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('admins.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('admins.do_index'))
    return render_template('login.html', title='Sign In', form=form)


@adm.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admins.do_index'))


@adm.route('/')
def admin_root():
    # do something
    return render_template('admins.html')


@adm.route('/index')
def do_index():
    return 'hello'


def index():
    return 'adm'
