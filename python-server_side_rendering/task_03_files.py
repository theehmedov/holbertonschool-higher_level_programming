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
# Əsas log mesajları üçün (məsələn, fayl tapılmadıqda)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s') 


def read_json(filename):
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


def read_csv(filename):
    """Reads data from a CSV file and returns a list of dictionaries."""
    data = []
    if not os.path.exists(filename):
        logging.error(f"CSV file not found: {filename}")
        return []
        
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV-dən oxunan id və price string olur.
                # JSON-a uyğun filtrləmə üçün string olaraq saxlayırıq.
                # Lakin Qiyməti float kimi yoxlamaq üçün bu hissə buraxılır.
                try:
                    row['id'] = str(row['id']) # ID-ni string saxla
                    row['price'] = float(row['price']) # Qiyməti float-a çevir
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

    # 1. Determine Source & Handle "Wrong source"
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    else:
        # 🟢 Düzəliş 1: Tam xəta mesajı
        error_message = "Wrong source. Please use 'json' or 'csv'."
        return render_template('product_display.html', error_message=error_message)

    # 2. Filter by ID if provided
    if product_id:
        # ID-ni string kimi filtrləmək
        # JSON-da id int, CSV-də string, query parametrdə string olduğundan, hər şeyi string-ə çeviririk.
        
        # ID-nin rəqəm olduğunu yoxlayırıq ki, "Product not found" mesajı daha dəqiq olsun
        try:
            # Sadece yoxlamaq ucun int-e ceviririk, filtrləmə string üzərindədir.
            int(product_id) 
        except ValueError:
             # ID formatı səhvdirsə, uyğun xəta qaytarırıq (Təlimatda xüsusi tələb olmasa da, yaxşı praktikadır)
             error_message = f"Invalid ID format provided: {product_id}."
             return render_template('product_display.html', error_message=error_message)
        
        filtered_products = [
            p for p in products_data 
            if str(p.get('id')) == str(product_id)
        ]
        
        if not filtered_products:
            # 🟢 Düzəliş 2: Tam xəta mesajı
            error_message = f"Product with ID {product_id} not found in the {source} data."
            products_data = [] # Boş siyahı göndərin
        else:
            products_data = filtered_products

    # 3. Handle data read failure (if list is unexpectedly empty after source check)
    if not products_data and error_message is None:
        if product_id is None:
             # Fayl boşdursa və ID filtri yoxdursa
             error_message = f"No data found in the {source} source file."
        
    # 4. Final Render
    return render_template('product_display.html', 
                           products=products_data, 
                           error_message=error_message)


@app.route('/')
def index():
    # Test asanlığı üçün marşrut
    return '<h1>Product System</h1><p>Test with: <a href="/products?source=json">JSON</a>, <a href="/products?source=csv&id=1">CSV ID 1</a>, <a href="/products?source=xml">Invalid Source</a></p>'


if __name__ == '__main__':
    app.run(debug=True, port=5000)#!/usr/bin/python3
"""
Flask application to display data from JSON or CSV files based on query parameters.
"""
from flask import Flask, render_template, request
import json
import csv
import os
import logging

app = Flask(__name__)
# Əsas log mesajları üçün (məsələn, fayl tapılmadıqda)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s') 


def read_json(filename):
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


def read_csv(filename):
    """Reads data from a CSV file and returns a list of dictionaries."""
    data = []
    if not os.path.exists(filename):
        logging.error(f"CSV file not found: {filename}")
        return []
        
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV-dən oxunan id və price string olur.
                # JSON-a uyğun filtrləmə üçün string olaraq saxlayırıq.
                # Lakin Qiyməti float kimi yoxlamaq üçün bu hissə buraxılır.
                try:
                    row['id'] = str(row['id']) # ID-ni string saxla
                    row['price'] = float(row['price']) # Qiyməti float-a çevir
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

    # 1. Determine Source & Handle "Wrong source"
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    else:
        # 🟢 Düzəliş 1: Tam xəta mesajı
        error_message = "Wrong source. Please use 'json' or 'csv'."
        return render_template('product_display.html', error_message=error_message)

    # 2. Filter by ID if provided
    if product_id:
        # ID-ni string kimi filtrləmək
        # JSON-da id int, CSV-də string, query parametrdə string olduğundan, hər şeyi string-ə çeviririk.
        
        # ID-nin rəqəm olduğunu yoxlayırıq ki, "Product not found" mesajı daha dəqiq olsun
        try:
            # Sadece yoxlamaq ucun int-e ceviririk, filtrləmə string üzərindədir.
            int(product_id) 
        except ValueError:
             # ID formatı səhvdirsə, uyğun xəta qaytarırıq (Təlimatda xüsusi tələb olmasa da, yaxşı praktikadır)
             error_message = f"Invalid ID format provided: {product_id}."
             return render_template('product_display.html', error_message=error_message)
        
        filtered_products = [
            p for p in products_data 
            if str(p.get('id')) == str(product_id)
        ]
        
        if not filtered_products:
            # 🟢 Düzəliş 2: Tam xəta mesajı
            error_message = f"Product with ID {product_id} not found in the {source} data."
            products_data = [] # Boş siyahı göndərin
        else:
            products_data = filtered_products

    # 3. Handle data read failure (if list is unexpectedly empty after source check)
    if not products_data and error_message is None:
        if product_id is None:
             # Fayl boşdursa və ID filtri yoxdursa
             error_message = f"No data found in the {source} source file."
        
    # 4. Final Render
    return render_template('product_display.html', 
                           products=products_data, 
                           error_message=error_message)


@app.route('/')
def index():
    # Test asanlığı üçün marşrut
    return '<h1>Product System</h1><p>Test with: <a href="/products?source=json">JSON</a>, <a href="/products?source=csv&id=1">CSV ID 1</a>, <a href="/products?source=xml">Invalid Source</a></p>'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
