'''api module for retrieving products data from index'''
from flask_restful import Resource, reqparse
from search import query_index


class Products(Resource):
    '''Products resource to find products according to querystring.'''

    # argument parser for product
    reqparser = reqparse.RequestParser()
    reqparser.add_argument(
        'q', required=True, type=str, help='Search text')
    reqparser.add_argument(
        'offset', required=True, type=int, help='Starting point')
    reqparser.add_argument(
        'limit', required=True, type=int, help='Number of products')

    def get(self):
        args = self.reqparser.parse_args()

        products, total_products = query_index(
            args['q'], args['offset'], args['limit'])

        return {
            'products': products,
            'totalProducts': total_products,
        }
