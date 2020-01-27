import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data - list of books I am planning/currently reading...
books = [
    {'id': 0,
     'title': 'Designing Data-Intensive Applications',
     'author': 'Martin Kleppmann',
     'first_sentence': 'Data is at the center of many challenges in system design today',
     'year_published': '2017'},
    {'id': 1,
     'title': 'Computer Networking: A Top-Down Approach',
     'author': 'Keith Ross',
     'first_sentence': 'Motivate your students with a top-down, layered approach to computer networking',
     'published': '2013'},
    {'id': 2,
     'title': 'Web Operations: Keeping the Data on Time',
     'author': 'John Allspaw',
     'first_sentence': 'wep operations',
     'published': '2010'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()
