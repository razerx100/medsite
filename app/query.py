from app.models import Admin, Category
from flask_login import login_user
from app import db


class Query:
    class AdminQuery:
        def __init__(self):
            pass

        def check_user(self, user, password):
            usr = Admin.query.filter_by(username=user).first()
            if usr is None or not usr.check_password(password):
                return False
            else:
                return True

        def login(self, user, memory):
            usr = Admin.query.filter_by(username=user).first()
            login_user(usr, memory)

    class CategoryQuery:
        def __init__(self):
            pass

        def save_category(self, data):
            cat = Category(
                Type=data[0],
                title=data[1],
                parent_cat=data[2],
                description=data[3],
                image=data[4],
                status=data[5],
            )
            db.session.add(cat)
            db.session.commit()

        def get_all_categories(self):
            return Category.query.all()

