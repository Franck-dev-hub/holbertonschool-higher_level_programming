#!/usr/bin/python3

from flask import Flask, render_template, request
import json, csv, sqlite3

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
    source = request.args.get("source")
    id = request.args.get("id")
    valid_sources = {"json": "json", "csv": "csv", "sql": "db"}
    items = []
    message = None
    product = None

    if source not in valid_sources:
        message = "Wrong source"

    else:
        extention = valid_sources[source]
        filename = "./products.{}".format(extention)
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
                elif source == "sql":
                    conn = sqlite3.connect(filename)
                    conn.row_factory = sqlite3.Row
                    cursor = conn.cursor()
                    cursor.execute("""
                        SELECT id, name, category, price
                        FROM Products
                        """)
                    items = [dict(row) for row in cursor.fetchall()]
                    conn.close()


        except FileNotFoundError:
            message= "File Not Found"
        except json.JSONDecodeError:
            message = "Invalid JSON format"
        except Exception as error:
            message = "Error reading data: {}".format(error)

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
