from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/dictionary/all')
def dictionary():
    return 'All the dictionaries'


@app.route('/dictionary/search/<word>')
def antonymDictionary(word):
    return 'The word youre searching for is %s' % escape(word)
