from flask import Flask, render_template
import json
import os
import logging

# Log formatını təyin edin
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

app = Flask(__name__)

# Köməkçi funksiya: JSON faylından məlumatları oxuyur
def get_items_data(filename='items.json'):
    """items.json faylından məlumatları oxuyur."""
    try:
        # Faylın mövcudluğunu yoxlayın
        if not os.path.exists(filename):
            logging.error(f"File not found: {filename}")
            return None
            
        with open(filename, 'r') as f:
            data = json.load(f)
            # Yalnız "items" açarındakı siyahını qaytarın
            return data.get("items", [])
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from {filename}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

# --- Əvvəlki tapşırıqdan olan marşrutlar (Task 1) ---

@app.route('/')
def home():
    # Başlıq və ayaq şablonlarını daxil etmək üçün index.html-i fərz edirik
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- Yeni Marşrut (Task 2) ---

@app.route('/items')
def items_list():
    """
    Items.json-dan məlumatları oxuyur və items.html şablonuna ötürür.
    """
    # Məlumatları oxuyun
    items = get_items_data()

    # Əgər oxuma uğursuz olarsa, boş siyahı ötürün (şərtin işləməsi üçün)
    if items is None:
        items = [] 
        
    # 'items' adlı dəyişəni şablona ötürün
    return render_template('items.html', items=items)

if __name__ == '__main__':
    # Tətbiqi debug rejimində və 5000 portunda işə sal
    app.run(debug=True, port=5000)
