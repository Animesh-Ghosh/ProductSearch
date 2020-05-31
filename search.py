'''Seach module for indexing products.json and querying the index.'''
import json
import os.path
from pprint import pprint
from whoosh import fields, qparser, index


class ProductSchema(fields.SchemaClass):
    '''Indexing schema for Products.'''
    ID = fields.NUMERIC(stored=True)
    image = fields.ID(stored=True)
    name = fields.TEXT(stored=True)
    description = fields.TEXT(stored=True)
    price = fields.NUMERIC(stored=True)


def create_index():
    # check if directory exits
    if not os.path.exists('index'):
        os.mkdir('index')

    ix = index.create_in('index', ProductSchema)

    with open('products.json', 'rb') as f:
        products = json.load(f)
        writer = ix.writer()

        for product in products['products']:
            writer.add_document(
                ID=product['id'],
                image=product['image'],
                name=product['name'],
                description=product['description'],
                price=product['price']
            )

        writer.commit()


def query_index(q, offset, limit):
    ix = index.open_dir('index')
    products = []

    with ix.searcher() as searcher:
        mp = qparser.MultifieldParser(
            ['name', 'description'], ix.schema)
        mpq = mp.parse(q)
        results = searcher.search_page(mpq, pagenum=offset + 1, pagelen=limit)

        for result in results:
            pprint(result)

            products.append({
                'id': result['ID'],
                'image': result['image'],
                'name': result['name'],
                'description': result['description'],
                'price': result['price']
            })

    return (products, len(results))
