import pandas as pd
import json
from app import db
from flask import request, jsonify
from app.models.books import Books, book_schema, books_schema
from io import StringIO
from Mq import Send



def insert_obras():
    title = request.json["titulo"]
    company = request.json["editora"]
    image = request.json["imagem"]
    authors = request.json["autores"]
    book = Books(title, company, image, authors)

    try:
        db.session.add(book)
        db.session.commit()
        result = book_schema.dump(book)
        return jsonify({"message": "Successfully insert", "data": result}), 201

    except:
        return jsonify({"message": "Unable to insert", "data": {}}), 500


def upload_obras():
    file = request.data.decode('utf-8')

    try:
        df = pd.read_csv(StringIO(file), sep=";")
        for row in df.index:
            book = Books(df.loc[row, "titulo"], df.loc[row, "editora"], df.loc[row, "imagem"], df.loc[row, "autores"])
            db.session.add(book)
            db.session.commit()
        return jsonify({"message": "Successfully insert"}), 201

    except Exception as error:
        return jsonify({"message": "Unable to insert", "data": {}}), 500, print(error)


def return_obras():
    books = Books.query.all()

    if books:
        result = books_schema.dump(books)
        return jsonify({"Message": "successfully request", "data": result}), 200

    return jsonify({'message': 'Unable to request', 'data': {}}), 500


def update_obras(id):
    book = Books.query.filter(Books.id == id).one()
    if not book:
        return jsonify({"message": "book don't exist"})

    try:
        book.title = request.json["titulo"]
        book.company = request.json["editora"]
        book.image = request.json["imagem"]
        book.authors = request.json["autores"]
        db.session.commit()
        result = book_schema.dump(book)
        return jsonify({'message': "Successfully updated", 'data': result}), 200

    except:
        return jsonify({'message': 'Unable to update', 'data': {}}), 500


def delete_obras(id):
    book = Books.query.filter(Books.id == id).one()
    if not book:
        return jsonify({"message": "book don't exist"})

    try:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'successfully delete'}), 204

    except:
        return jsonify({'message': 'Unable to request', 'data': {}}), 500


"""def request_email():
    books = Books.query.all()
    email = request.json["email"]
    if books:
        result = books_schema.dump(books)
        Send.send(body=json.dumps({"email": email, "books": result}))
        return jsonify({"Message": "successfully request", "data": result}), 200

    return jsonify({'message': 'Unable to request', 'data': {}}), 500"""