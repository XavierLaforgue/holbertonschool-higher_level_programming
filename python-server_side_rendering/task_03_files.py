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
            products = json.load(f).get('products')
            for product in products:
                for k, v in product.items():
                    if not isinstance(v, str):
                        product[k] = str(v)
    elif source == 'csv':
        with open('products.csv', 'r', encoding='utf-8') as f:
            products = list(csv.DictReader(f))
    else:
        return render_template('product_display.html',
                               error_source='Wrong source'), 400
    if product_id is not None:
        chosen_product = []
        for product in products:
            print(product)
            if product_id == product.get('id'):
                chosen_product = [product]
                break
        if chosen_product == [] or chosen_product[0].get('id') != product_id:
            return render_template('product_display.html',
                               error_id='Product not found'), 400
    return render_template('product_display.html', products=products), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
