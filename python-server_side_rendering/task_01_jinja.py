from flask import Flask, render_template

# Flask tətbiqinin yaradılması
app = Flask(__name__)

# Kök (Root) səhifə marşrutu
@app.route('/')
def home():
    # index.html şablonunu göstər
    return render_template('index.html')

# Haqqımızda (About) səhifə marşrutu
@app.route('/about')
def about():
    # about.html şablonunu göstər
    return render_template('about.html')

# Əlaqə (Contact) səhifə marşrutu
@app.route('/contact')
def contact():
    # contact.html şablonunu göstər
    return render_template('contact.html')

if __name__ == '__main__':
    # Tətbiqi debug rejimində və 5000 portunda işə sal
    # Tələb: app.run(debug=True, port=5000)
    app.run(debug=True, port=5000)
