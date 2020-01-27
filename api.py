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

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
