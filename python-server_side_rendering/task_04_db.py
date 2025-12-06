#!/usr/bin/python3
"""
Flask application extending dynamic data display to include SQLite.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# --- Verilənlər Bazasının Qurulması ---

def create_database(db_name='products.db'):
    """SQLite verilənlər bazasını yaradır və məlumatlarla doldurur."""
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Cədvəli yaradın (əgər mövcud deyilsə)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # Məlumatları daxil edin (ID 1 və 2 üçün)
        # INSERT OR IGNORE, eyni ID ilə təkrar daxil etməyin qarşısını alır
        cursor.execute("INSERT OR IGNORE INTO Products (id, name, category, price) VALUES (?, ?, ?, ?)",
                       (1, 'Laptop', 'Electronics', 799.99))
        cursor.execute("INSERT OR IGNORE INTO Products (id, name, category, price) VALUES (?, ?, ?, ?)",
                       (2, 'Coffee Mug', 'Home Goods', 15.99))
        
        conn.commit()
        logging.info("Database 'products.db' created and populated successfully.")
    except sqlite3.Error as e:
        logging.error(f"SQLite error during database creation: {e}")
    finally:
        if conn:
            conn.close()

# --- Məlumat Oxuma Funksiyaları ---

# Task 3-dən: JSON oxuma (məzmunu buraya kopyalayın)
def read_json(filename='products.json'):
    """Reads data from a JSON file."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception:
        return []

# Task 3-dən: CSV oxuma (məzmunu buraya kopyalayın)
def read_csv(filename='products.csv'):
    """Reads data from a CSV file and returns a list of dictionaries."""
    data = []
    if not os.path.exists(filename):
        return []
        
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['id'] = str(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
                except ValueError:
                    continue
        return data
    except Exception:
        return []

# 🟢 Yeni: SQLite oxuma funksiyası
def read_sql(product_id=None, db_name='products.db'):
    """Reads data from the SQLite database."""
    conn = None
    data = []
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row # Sütun adlarını istifadə etməyə imkan verir
        cursor = conn.cursor()
        
        query = "SELECT id, name, category, price FROM Products"
        params = ()
        
        if product_id:
            query += " WHERE id = ?"
            params = (product_id,)
            
        cursor.execute(query, params)
        
        # Məlumatları lüğətlər siyahısı kimi formatlayın
        for row in cursor.fetchall():
            data.append({
                'id': row['id'], 
                'name': row['name'], 
                'category': row['category'], 
                'price': row['price']
            })
        return data
        
    except sqlite3.Error as e:
        logging.error(f"SQLite database error: {e}")
        return None # None qaytarın ki, əsas funksiya xətanı idarə etsin
    finally:
        if conn:
            conn.close()

# --- Flask Route ---

@app.route('/products')
def products():
    """
    Route to display products based on source (json/csv/sql) and optional id.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    products_data = None # None ilə başla, oxuma xətalarını idarə etmək üçün
    error_message = None

    # ID-ni yalnız filtrləmə üçün istifadə etmək üçün int-ə çevirin
    product_id_int = None
    if product_id_str:
        try:
            # SQL DB-də ID-lər int-dir.
            product_id_int = int(product_id_str) 
        except ValueError:
            error_message = f"Invalid ID format provided: {product_id_str}."
            return render_template('product_display.html', error_message=error_message)


    # 1. Mənbəni müəyyənləşdirin
    if source == 'json':
        products_data = read_json()
    elif source == 'csv':
        products_data = read_csv()
    elif source == 'sql':
        # 🟢 Yeni: SQL mənbəyindən oxuma
        # SQL funksiyasında filtrləməni (ID varsa) həyata keçiririk
        products_data = read_sql(product_id=product_id_int) 
    else:
        # ⚠️ Yanlış Mənbə
        error_message = "Wrong source. Please use 'json', 'csv', or 'sql'."
        return render_template('product_display.html', error_message=error_message)

    
    # Məlumat oxunması zamanı xətanın idarə edilməsi (read_sql None qaytara bilər)
    if products_data is None:
         error_message = f"An error occurred while reading from the {source} data source."
         return render_template('product_display.html', error_message=error_message)

    # 2. ID-yə görə filtrləmə (yalnız JSON və CSV üçün lazımdır, SQL artıq filtrlənib)
    if source != 'sql' and product_id_int:
        # JSON/CSV datası string ID-lərə malik ola bilər
        filtered_products = [
            p for p in products_data
            if str(p.get('id')) == str(product_id_int)
        ]
        
        if not filtered_products:
            error_message = "Product not found"
            products_data = []
        else:
            products_data = filtered_products
    # 3. SQL halında, filtrləmə read_sql funksiyasının içində edilir.
    
    # 4. Əgər ID sorğulanıb, məlumat boşdursa və xəta mesajı yoxdursa (SQL-də ID tapılmaması)
    if not products_data and product_id_int:
        error_message = "Product not found"
        
    # 5. Final Render
    return render_template('product_display.html', 
                           products=products_data, 
                           error_message=error_message)


@app.route('/')
def index():
    return '<h1>Product System</h1><p>Test sources: <a href="/products?source=json">JSON</a> | <a href="/products?source=csv">CSV</a> | <a href="/products?source=sql">SQL</a></p>'


if __name__ == '__main__':
    # ⚠️ Tətbiqi işə salmadan əvvəl verilənlər bazasını yaradın
    create_database()
    app.run(debug=True, port=5000)
