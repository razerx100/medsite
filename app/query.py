from app.models import Admin
from flask_login import login_user

class Query:
    class UserQuery:
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

