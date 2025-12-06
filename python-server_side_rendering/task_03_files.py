from flask import Flask, render_template, request
import json
import csv
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# --- Məlumat Oxuma Funksiyaları ---

def read_json_data(filename='products.json'):
    """JSON faylından məlumatı oxuyur və siyahı qaytarır."""
    if not os.path.exists(filename):
        logging.error(f"JSON file not found: {filename}")
        return None
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logging.error(f"Error reading or decoding JSON file: {e}")
        return None

def read_csv_data(filename='products.csv'):
    """CSV faylından məlumatı oxuyur və lüğətlər siyahısı qaytarır."""
    if not os.path.exists(filename):
        logging.error(f"CSV file not found: {filename}")
        return None
    data = []
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # İD və qiyməti uyğun olaraq integer və float-a çevirin
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    # Məlumatın formatı səhvdirsə, bu sıranı atlayaq
                    continue
                data.append(row)
        return data
    except IOError as e:
        logging.error(f"Error reading CSV file: {e}")
        return None

# --- Süzgəcdən Keçirmə Məntiqi ---

def filter_products(products, product_id):
    """Məhsulları verilmiş ID-yə əsasən süzgəcdən keçirir."""
    if not products or product_id is None:
        return products
    
    # ID-nin tam ədəd olduğundan əmin olun
    try:
        pid = int(product_id)
    except ValueError:
        return [] # Yanlış ID formatı

    filtered = [p for p in products if p.get('id') == pid]
    return filtered

# --- Flask Route ---

@app.route('/products')
def products():
    """
    /products marşrutu JSON və ya CSV faylından məlumatları oxuyur,
    ID-yə görə süzgəcdən keçirir və göstərir.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    product_id = None

    # ID parametrini tam ədədə çevirin
    if product_id_str:
        try:
            product_id = int(product_id_str)
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format provided.")

    # 1. Mənbəni (Source) Yoxlayın və Məlumatı Oxuyun
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    else:
        # 4. Yanlış Mənbənin İdarə Edilməsi
        return render_template('product_display.html', error="Wrong source. Please use 'json' or 'csv'.")

    # Məlumat oxunarkən səhv baş verərsə
    if products_data is None:
        return render_template('product_display.html', error=f"Could not load data from {source} source.")

    # 2. Məlumatı Süzgəcdən Keçirin
    filtered_products = filter_products(products_data, product_id)

    # 3. ID tapılmazsa Xətanın İdarə Edilməsi
    if product_id is not None and not filtered_products:
        return render_template('product_display.html', error=f"Product with ID {product_id} not found in the {source} data.")

    # 5. Məlumatı Şablona Ötürün
    return render_template('product_display.html', products=filtered_products)

# Əsas marşrut (test üçün)
@app.route('/')
def index():
    return '<h1>Welcome to the Product System</h1><p>Test with: <ul><li><a href="/products?source=json">JSON (All)</a></li><li><a href="/products?source=csv&id=2">CSV (ID 2)</a></li><li><a href="/products?source=xml">Invalid Source</a></li></ul></p>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
