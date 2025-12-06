#!/usr/bin/python3
"""
Flask application to display data from JSON or CSV files based on query parameters.
"""
from flask import Flask, render_template, request
import json
import csv
import os
import logging

app = Flask(__name__)
# Logları təyin et (isteğe bağlı, amma yaxşı praktikadır)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def read_json(filename='products.json'):
    """Reads data from a JSON file."""
    if not os.path.exists(filename):
        logging.error(f"JSON file not found: {filename}")
        return []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error reading or decoding JSON file: {e}")
        return []


def read_csv(filename='products.csv'):
    """Reads data from a CSV file and returns a list of dictionaries."""
    data = []
    if not os.path.exists(filename):
        logging.error(f"CSV file not found: {filename}")
        return []
        
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Qiyməti float-a çevirməyə çalışırıq
                try:
                    row['id'] = str(row['id']) # ID-ni string kimi saxlayırıq
                    row['price'] = float(row['price'])
                    data.append(row)
                except ValueError:
                    logging.warning(f"Skipping row due to invalid number format: {row}")
                    continue
        return data
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        return []


@app.route('/products')
def products():
    """
    Route to display products based on source (json/csv) and optional id.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products_data = []
    error_message = None

    # 1. Mənbəni müəyyənləşdirin və "Wrong source" xətasını idarə edin
    if source == 'json':
        products_data = read_json()
    elif source == 'csv':
        products_data = read_csv()
    else:
        # 🟢 Düzəliş 1: Tam tələb olunan cümlə
        error_message = "Wrong source. Please use 'json' or 'csv'."
        return render_template('product_display.html', error_message=error_message)


    # 2. ID filtrlənməsi (əgər təmin olunubsa)
    if product_id:
        # ID-ni string kimi filtrləyin
        filtered_products = [
            p for p in products_data 
            if str(p.get('id')) == str(product_id)
        ]
        
        if not filtered_products:
            # 🟢 Düzəliş 2: Təlimatda tələb olunan sadə xəta mətni
            error_message = "Product not found" 
            products_data = [] # Boş siyahı göndərin
        else:
            products_data = filtered_products

    # 3. Final Render (products_data hər hansı bir filtrləmədən sonra məhsulları ehtiva edir)
    return render_template('product_display.html', 
                           products=products_data, 
                           error_message=error_message)


@app.route('/')
def index():
    # Test asanlığı üçün marşrut
    return '<h1>Product System</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
