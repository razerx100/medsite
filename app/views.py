from app import webapp
from flask import render_template, url_for, redirect
from app.forms import LoginForm


@webapp.route("/favicon.ico")
def fav_ico():
    return url_for("static", filename="img/icon/icon.png")


@webapp.route("/")
def homepage():
    return render_template("homepage.html", title="Mr. Med Home")


@webapp.route("/admin")
def admin_page():
    return render_template("admin_page.html", title="Mr. Med Admin")


@webapp.route("/login", methods=["POST", "GET"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("homepage"))
    return render_template("login_page.html", title="Login", form=form)
