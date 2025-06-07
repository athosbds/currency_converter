from flask import Flask, render_template, request
from models import CurrencyConverter
app = Flask(__name__)

base_url = 'https://api.exchangerate-api.com/v4/latest/'

API_URLS = {
    'USD': base_url + 'USD',
    'GBP': base_url + 'GBP',
    'EUR': base_url + 'EUR',
}

converter = CurrencyConverter(API_URLS)

@app.route('/')
def index():
    result = None
    error = None
    return render_template('index.html', result=result, error=error)
if __name__ == "__main__":
    app.run(debug=True)
