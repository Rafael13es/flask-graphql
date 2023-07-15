"""Bookshop"""
from app import db
from app.routes import app
from app.models import Book


@app.shell_context_processor
def make_shell_context():
    """
    returns a dictionary that contains the db and Book instances that we need to add to the shell
    session to use them in the shell without having to import them
    :return: a dictionary of db and book
    """
    return {"db": db, "Book": Book}
