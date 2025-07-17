from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        items_in_json = json.load(f)
    return render_template('items.html', items=items_in_json.get('items'))

@app.route('/products')
def products():
    source = request.args.get('source', None)
    product_id = request.args.get('id', None)
    if source == 'json':
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
            for product in products:
                for k, v in product.items():
                    if not isinstance(v, str):
                        product[k] = str(v)
        print(f'entered source=json product={products}')
    elif source == 'csv':
        with open('products.csv', 'r', encoding='utf-8') as f:
            products = list(csv.DictReader(f))
        print(f'entered source=csv product={products}')
    else:
        print('entered source=bad source')
        return render_template('product_display.html',
                               error_source='Wrong source'), 200
    if product_id is not None:
        print('entered product_id not none')
        # chosen_product = []
        for product in products:
            print('entered product loop')
            if product_id == product.get('id'):
                # chosen_product = [product]
                products = [product]
                # print(f'entered product_id=product.get(id) condition and
                # chosen_product={chosen_product}')
                print(f'entered product_id=product.get(id) condition and products={products}')
                break
        # if chosen_product == [] or chosen_product[0].get('id') != product_id:
            # print('entered empty chosen_product or product_id different from chosen_product.get(id)')
            # return render_template('product_display.html',
            #                    error_id='Product not found'), 400
        if len(products) != 1 or products[0].get('id') != product_id:
            print('entered number of products different than 1 or product_id different from product.get(id)')
            return render_template('product_display.html',
                                   error_id='Product not found'), 200
    print(f'not entered product_id not none products={products}')
    return render_template('product_display.html', products=products), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
