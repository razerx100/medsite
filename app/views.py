import os
from app import webapp
from flask import render_template, url_for, redirect, flash, request
from app.forms import LoginForm, AddCategoriesForm, AddManufacturerForm, AddProductForm
from app.query import Query
from flask_login import login_required, logout_user, current_user
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in [
        "png",
        "jpg",
        "jpeg",
    ]


@webapp.route("/favicon.ico")
def fav_ico():
    return url_for("static", filename="img/icon/icon.png")


@webapp.route("/")
def homepage():
    return render_template("homepage.html", title="Mr. Med Home")


@webapp.route("/admin", methods=["POST", "GET"])
@login_required
def admin_page():
    forms = [AddCategoriesForm(), AddManufacturerForm(), AddProductForm()]
    if request.method == "POST":
        if forms[0].validate():
            img_name = None
            if request.files:
                image = request.files["image"]
                if image and allowed_file(image.filename):
                    image_name = secure_filename(image.filename)
                    image.save(
                        os.path.join(
                            webapp.config["UPLOAD_FOLDER"] + "category_img", image_name
                        )
                    )
                    img_name = image_name

            data = [
                forms[0].Type.data,
                forms[0].title.data,
                forms[0].parent_cat.data,
                forms[0].description.data,
                img_name,
                forms[0].status.data,
            ]
            Query.CategoryQuery().save_category(data)
            return render_template(
                "admin_page.html",
                title="Mr. Med Admin",
                forms=forms,
                landing=".cat_stuff",
                categories=Query.CategoryQuery().get_all_categories(),
            )
        elif forms[1].validate():
            return render_template(
                "admin_page.html",
                title="Mr. Med Admin",
                forms=forms,
                landing=".manu_stuff",
            )
        elif forms[2].validate():
            return render_template(
                "admin_page.html",
                title="Mr. Med Admin",
                forms=forms,
                landing=".prod_stuff",
            )
        # else:
        #     return render_template("admin_page.html", title="Mr. Med Admin", forms=forms, landing=".add_cat")
    return render_template(
        "admin_page.html",
        title="Mr. Med Admin",
        forms=forms,
        landing=".dash_stuff",
        categories=Query.CategoryQuery().get_all_categories(),
    )


@webapp.route("/login", methods=["POST", "GET"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("homepage"))
    form = LoginForm()
    if form.validate_on_submit():
        if Query.AdminQuery().check_user(form.username.data, form.password.data):
            Query.AdminQuery().login(form.username.data, form.remember_me.data)
        else:
            flash("Username or password doesn't exists.")
            return redirect(url_for("login_page"))
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("homepage")
        return redirect(next_page)
    return render_template("login_page.html", title="Login", form=form)


@webapp.route("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("homepage"))
