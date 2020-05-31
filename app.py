'''app module for running Flask server and serving index.html.'''
import json
from flask import Flask, render_template, jsonify
from flask_restful import Api
from whoosh.index import create_in
from whoosh.fields import *
from api import Products
from search import create_index

app = Flask(__name__)
api = Api(app)

api.add_resource(Products, '/api/v1/product/search')


@app.route('/')
def index():
    '''View to render the index page.'''
    return render_template('index.html')


@app.route('/api/v1/product/index')
def index_products():
    '''View to index the products.json file.'''

    create_index()

    return jsonify({
        'message': 'Indexing complete!',
    })
