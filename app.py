import json
from flask import Flask, render_template, jsonify
from flask_restful import Api
from api import Products

app = Flask(__name__)
api = Api(app)

api.add_resource(Products, '/api/v1/product/search')


@app.route('/')
def index():
    '''View to render the index page.'''
    return render_template('index.html')


@app.route('/api/v1/product/index')
def index_products():
    '''View to index the products.json file and return a list of products'''
    with open('products.json', 'rb') as f:
        products = json.load(f)

    # indexing code using whoosh

    return jsonify({
        'message': 'Indexing Products for keyword search...',
    })
