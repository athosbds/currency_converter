from flask import Flask, render_template, request
from models import CurrencyConverter
app = Flask(__name__)

base_url = 'https://api.exchangerate-api.com/v4/latest/'

API_URLS = {
    'USD': base_url + 'USD',
    'GBP': base_url + 'GBP',
    'EUR': base_url + 'EUR',
}


@app.route('/')
def index():
    amount = None
    error = None
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
