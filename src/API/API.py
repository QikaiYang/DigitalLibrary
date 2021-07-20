"""
The structure of my code in this file comes from
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
"""

import flask
from flask import request, make_response, jsonify
from Database.Database import Database
import json


def api(db):
    app = flask.Flask(__name__)
    books_raw = db.get("Book")
    authors_raw = db.get("Author")
    books = []
    authors = []
    preprocess(books, books_raw)
    preprocess(authors, authors_raw)

    @app.route('/', methods=['GET'])
    def home():
        """
        Home Page
        :return: return the raw code of the home page of Qikai's API
        """
        return '''<h1>CS 242</h1>
            <p>Qikai's API of Assignment 2.1</p>'''

    @app.route('/books/all', methods=['GET'])
    def api_book_all():
        """
        GET all books and show it in the API page
        :return: return the raw code of all the books
        """
        return jsonify(books)

    @app.route('/authors/all', methods=['GET'])
    def api_author_all():
        """
        GET all authors and show it in the API page
        :return: return the raw code of all the authors
        """
        return jsonify(authors)

    @app.route('/books', methods=['GET'])
    def api_book_id():
        """
        GET the book with certain ID and show it in the API page
        :return: return the raw code of the book with certain ID
        """
        if 'id' in request.args:
            id_req = int(request.args['id'])
        else:
            return make_response(jsonify({"Error": "Book not found"}), 400)
        results = []
        for book in books:
            if book['id'] == id_req:
                results.append(book)
        return jsonify(results)

    @app.route('/authors', methods=['GET'])
    def api_author_id():
        """
        GET the author with certain ID and show it in the API page
        :return: return the raw code of the author with certain ID
        """
        if 'id' in request.args:
            id_req = int(request.args['id'])
        else:
            return make_response(jsonify({"Error": "Author not found"}), 400)
        results = []
        for author in authors:
            if author['id'] == id_req:
                results.append(author)
        return jsonify(results)

    @app.route('/books/add', methods=['POST'])
    def api_post_book():
        """
        POST the book
        :return: return the posted book
        """
        data = request.get_json()
        books.append(data)
        return jsonify(data)

    @app.route('/authors/add', methods=['POST'])
    def api_post_author():
        """
        POST the author
        :return: return the posted author
        """
        data = request.get_json()
        authors.append(data)
        return jsonify(data)

    @app.route('/books/delete', methods=['DELETE'])
    def api_delete_book():
        """
        DELETE the book with certain ID and show it in the API page
        :return: return the raw code of the book with certain ID
        """
        if 'id' in request.args:
            id_req = int(request.args['id'])
        else:
            return make_response(jsonify({"Error": "Book not found"}), 400)
        results = []
        for book in books:
            if book['id'] == id_req:
                results.append(book)
        return jsonify(list(set(books) - set(results)))

    @app.route('/authors/delete', methods=['DELETE'])
    def api_delete_author():
        """
        DELETE the author with certain ID and show it in the API page
        :return: return the raw code of the author with certain ID
        """
        if 'id' in request.args:
            id_req = int(request.args['id'])
        else:
            return make_response(jsonify({"Error": "Author not found"}), 400)
        results = []
        for author in authors:
            if author['id'] == id_req:
                results.append(author)
        return jsonify(list(set(authors) - set(results)))

    @app.route('/books/put', methods=['PUT'])
    def api_put_book():
        """
        PUT the book with certain ID and show it in the API page
        :return: return the raw code of the book with certain ID
        """
        if 'id' in request.args:
            id_req = int(request.args['id'])
        else:
            return make_response(jsonify({"Error": "Book not found"}), 400)
        for book in books:
            if book['id'] == id_req:
                books[books.index(book)] = request.get_json()
        db.delete("/Book")
        for i in books:
            db.write("Book", i)
        return jsonify(books)

    @app.route('/authors/put', methods=['PUT'])
    def api_put_author():
        """
        PUT the author with certain ID and show it in the API page
        :return: return the raw code of the author with certain ID
        """
        if 'id' in request.args:
            id_req = int(request.args['id'])
        else:
            return make_response(jsonify({"Error": "Author not found"}), 400)
        for author in authors:
            if author['id'] == id_req:
                authors[authors.index(author)] = request.get_json()
        db.delete("/Author")
        for i in authors:
            db.write("Author", i)
        return jsonify(authors)

    app.run()


def preprocess(dest, raw_data):
    """
    Preprocess raw data to make it into a dictionary
    :param dest: the dictionary to be put
    :param raw_data: input raw fata from database
    :return:
    """
    for k in list(raw_data.keys()):
        tmp = json.loads(raw_data[k])
        tmp["id"] = int(tmp["id"])
        dest.append(tmp)


# db = Database("https://cs242-97d35-default-rtdb.firebaseio.com/")
# api(db)
