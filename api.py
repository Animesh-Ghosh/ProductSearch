import json
from pprint import pprint
from flask_restful import Resource, reqparse

# argument parser for product
product_reqparser = reqparse.RequestParser()
product_reqparser.add_argument('q', required=True, type=str, help='Search text')
product_reqparser.add_argument('offset', required=True, type=int, help='Starting point')
product_reqparser.add_argument('limit', required=True, type=int, help='Number of products')


class Products(Resource):
    def get(self):
        args = product_reqparser.parse_args()

        with open('products.json', 'rb') as f:
            products = json.load(f)

        total_products = len(products['products'])

        products = list(filter(
            lambda x: x['id'] > args['offset'] and x['id'] <= args['offset'] + args['limit'],
            products['products']
        ))

        return {
            'products': products,
            'totalProducts': total_products,
        }
