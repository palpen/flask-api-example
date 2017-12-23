import json
import sqlite3
from flask import Flask, request, g
from .utils import json_response, JSON_MIME_TYPE


app = Flask(__name__)


@app.before_request
def before_request():
    # initialize database that will be used across the view functions below (stored in g.db)
    g.db = sqlite3.connect(app.config['DATABASE_NAME'])


@app.route('/book')
def book_list():
    cursor = g.db.execute('SELECT id, author_id, title FROM book;')
    books = [{
        'id': row[0],
        'author_id': row[1],
        'title': row[2]
    } for row in cursor.fetchall()]

    return json_response(json.dumps(books))


@app.route('/book', methods=['POST'])
def book_create():
    """Insert data in database using the API"""

    # check if the posted data is a json data and not any other type of data
    # request is a global object that gives you access to the requested data by the the web client
    if request.content_type != JSON_MIME_TYPE:
        error = json.dumps({'error': 'Invalid Content Type'})
        return json_response(error, 400)

    # check if posted data has info in all required fields
    data = request.json
    if not all([data.get('title'), data.get('author_id')]):
        error = json.dumps({'error': 'Missing field/s (title, author_id)'})
        return json_response(error, 400)

    # database specific procedures
    query = ('INSERT INTO book ("author_id", "title") '
             'VALUES (:author_id, :title);')
    params = {
        'title': data['title'],
        'author_id': data['author_id']
    }
    g.db.execute(query, params)
    g.db.commit()

    return json_response(status=201)
