"""Routes"""

import os
from flask import jsonify, abort, request
from app.models import Book
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route("/book/list", methods=["GET"])
def get_books():
    """
        Get books from database
            :return: A list of books
            :rtype: Response
    """
    books = Book.query.all()
    return jsonify([book.to_json() for book in books])


@app.route("/book/<int:isbn>", methods=["GET"])
def get_book(isbn: int):
    """
        Get a book by its id
            :parameter int isbn: book id
            :return: A response
            :rtype: Response
    """
    book = Book.query.get(isbn)
    if book is None:
        abort(404)
    return jsonify(book.to_json())


@app.route('/book', methods=['POST'])
def create_book():
    """Create a book"""
    if not request.json:
        abort(400)
    book = Book(
        title=request.json.get('title'),
        author=request.json.get('author'),
        price=request.json.get('price')
    )
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_json()), 201


@app.route('/book/<int:isbn>', methods=['PUT'])
def update_book(isbn):
    """
    Updates a book
    :param isbn:
    :return: a response
    """
    if not request.json:
        abort(400)
    book = Book.query.get(isbn)
    if book is None:
        abort(404)
    book.title = request.json.get('title', book.title)
    book.author = request.json.get('author', book.author)
    book.price = request.json.get('price', book.price)
    db.session.commit()
    return jsonify(book.to_json())


@app.route("/book/<int:isbn>", methods=["DELETE"])
def delete_book(isbn):
    """
    Delete a book
    :param isbn:
    :return: a response
    """
    book = Book.query.get(isbn)
    if book is None:
        abort(404)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'result': True})
