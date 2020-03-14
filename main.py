from app import webapp, db
from app.models import Admin, Category

@webapp.shell_context_processor
def make_shell_context():
    return {"db" : db, "Admin": Admin, "Category": Category}
