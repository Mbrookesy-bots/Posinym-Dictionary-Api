from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../dictionary.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(80), unique=True)
    antonym = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.word = username
        self.antonym = email


class DictionarySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('word', 'antonym')


dictionary_schema = DictionarySchema()
dictionaries_schema = DictionarySchema(many=True)


# endpoint to create new user
@app.route("/dictionary", methods=["POST"])
def add_user():
    word = request.json['word']
    antonym = request.json['antonym']

    new_word = Dictionary(word, antonym)

    db.session.add(new_word)
    db.session.commit()

    return dictionary_schema.jsonify(new_word)


# endpoint to show all users
@app.route("/dictionary", methods=["GET"])
def get_word():
    all_words = Dictionary.query.all()
    result = dictionaries_schema.dump(all_words)
    return jsonify(result)


# endpoint to get user detail by id
@app.route("/dictionary/<id>", methods=["GET"])
def word_detail(id):
    word = Dictionary.query.get(id)
    return dictionary_schema.jsonify(word)


# endpoint to update user
@app.route("/dictionary/<id>", methods=["PUT"])
def word_update(id):
    dictionary = Dictionary.query.get(id)
    word = request.json['word']
    antonym = request.json['antonym']

    dictionary.antonym = antonym
    dictionary.word = word

    db.session.commit()
    return dictionary_schema.jsonify(dictionary)


# endpoint to delete user
@app.route("/dictionary/<id>", methods=["DELETE"])
def word_delete(id):
    word = Dictionary.query.get(id)
    db.session.delete(word)
    db.session.commit()

    return dictionary_schema.jsonify(word)


if __name__ == '__main__':
    app.run(debug=True)