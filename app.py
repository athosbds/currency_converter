from flask import Flask, render_template, request
from models import CurrencyConverter
app = Flask(__name__)
converter = CurrencyConverter()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    try:
        if request.method == 'POST':
            amount = float(request.form.get('amount', 0))
            from_currency = request.form.get('from_currency')
            to_currency = request.form.get('to_currency')
            result = converter.convert(amount, from_currency, to_currency)
    except ValueError:
        error = 'Valor Inválido'
    except Exception as e:
        error = str(e)
    return render_template('index.html', result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
