#!/usr/bin/python3

from flask import Flask, render_template, request
import json, csv

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
    filename = "./items.json"
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            items = json.loads(file.read())["items"]
    except (FileNotFoundError, KeyError):
        items = []
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get("source").lower().strip()
    id = request.args.get("id")
    valid_sources = ["json", "csv"]
    items = []
    message = None
    product = None

    if source not in valid_sources:
        message = "Wrong source"

    else:
        filename = "./products.{}".format(source)
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                if source == "json":
                    items = json.loads(file.read())
                elif source == "csv":
                    data = csv.DictReader(file)
                    for row in data:
                        row["id"] = int(row["id"])
                        row["price"] = float(row["price"])
                        items.append(row)
        except FileNotFoundError:
            message= "File Not Found"
        except json.JSONDecodeError:
            message = "Invalid JSON format"

        if id and not message:
            try:
                id = int(id)
                for item in items:
                    if item.get("id") == id:
                        product = item
                        break

                if product is None:
                    message = "Product not found"
                    items = []
            except ValueError:
                message = "Invalid id parameter : {}".format(id)
                items = []

    return render_template('product_display.html', items=items, id=id, message=message)

if __name__ == '__main__':
   app.run(debug=True, port=5000)
