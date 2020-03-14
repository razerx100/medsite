from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    SelectField,
    TextAreaField,
    FileField,
    RadioField,
)
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    password_re = PasswordField("Re Enter Password", [DataRequired()])
    email = StringField("Email", [DataRequired()])
    register = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    remember_me = BooleanField("Remember me")
    login = SubmitField("Login")


class AddCategoriesForm(FlaskForm):
    Type = SelectField(
        "Type", choices=[("presc", "Prescriptions"), ("meds", "Medical Products")]
    )
    title = StringField("Categories Title", validators=[DataRequired()])
    parent_cat = SelectField(
        "Parent Category", choices=[("----", "No Parent"), ("par1", "Good Parent")]
    )
    description = TextAreaField("Categories Description", validators=[DataRequired()])
    image = FileField("Categories Image:")
    status = RadioField(
        "Set Category Status", choices=[("active", "Active"), ("inactive", "Inactive")]
    )
    submit = SubmitField("Add Category")


class AddManufacturerForm(FlaskForm):
    name = StringField("Manufacturer Name:", [DataRequired()])
    image = FileField("Manufacturer Image:")
    submit = SubmitField("Add Manufacturer")


class AddProductForm(FlaskForm):
    title = StringField("Product Title :", [DataRequired()])
    category = SelectField(
        "Product Category :", choices=[("----", "Select Category"), ("dum", "Cat1")]
    )
    manufacturer = SelectField(
        "Manufacturer:*", choices=[("----", "Select Manufacturer"), ("dam", "Manu1")]
    )
    image = FileField("Product Image:")
    generic = BooleanField("is Generic")
    status = RadioField(
        "Set Product status",
        choices=[("stock_in", "In stock"), ("stock_out", "Out of stock")],
    )
    price = StringField("Price :", [DataRequired()])
    unit = StringField("Unit :", [DataRequired()])
    submit = SubmitField("Add Product")
