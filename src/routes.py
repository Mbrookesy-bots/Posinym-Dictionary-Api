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
    antonym = db.Column(db.String(120))

    def __init__(self, username, email):
        self.word = username
        self.antonym = email


class DictionarySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('word', 'antonym')


dictionary_schema = DictionarySchema()
dictionaries_schema = DictionarySchema(many=True)

# endpoint to get user detail by name
@app.route("/dictionary", methods=["GET"])
def word_query():
    word_arg = request.args['word']
    word = Dictionary.query.filter_by(word=word_arg).first()

    if word == None:
        return jsonify(antonym=word_arg)
    else:
        return dictionary_schema.jsonify(word)

if __name__ == '__main__':
    app.run(debug=True)