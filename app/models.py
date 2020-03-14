from app import db, login_mnr
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

@login_mnr.user_loader
def current_user(id):
    return Admin.query.get(int(id))

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<Admin {self.username}>"

    def generate_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(128), unique=True, index=True)
    Title = db.Column(db.String(512), unique=True, index=True)
    parent_cat = db.Column(db.String(128))
    description = db.Column(db.String(1024))
    image = db.Column(db.String(520), unique=True, index=True)
    status = db.Column(db.String((16)))

    def __repr__(self):
        return f"<Category {self.Title}>"
