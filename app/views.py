from app import webapp, db
from flask import render_template, url_for, redirect, flash, request
from app.forms import LoginForm
from app.models import Admin
from app.query import Query
from flask_login import login_required, logout_user, current_user
from werkzeug.urls import url_parse

@webapp.route("/favicon.ico")
def fav_ico():
    return url_for("static", filename="img/icon/icon.png")


@webapp.route("/")
def homepage():
    return render_template("homepage.html", title="Mr. Med Home")


@webapp.route("/admin")
@login_required
def admin_page():
    return render_template("admin_page.html", title="Mr. Med Admin")


@webapp.route("/login", methods=["POST", "GET"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        if Query.UserQuery().check_user(form.username.data, form.password.data):
            Query.UserQuery().login(form.username.data, form.remember_me.data)
        else:
            flash("Username or password doesn't exists.")
            return redirect(url_for('login_page'))
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("homepage")
        return redirect(next_page)
    return render_template("login_page.html", title="Login", form=form)

@webapp.route("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("homepage"))
