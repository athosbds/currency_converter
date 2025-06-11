import requests

class CurrencyConverter:
    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return round(amount, 2)
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        respo =  requests.get(url)
        if respo.status_code == 200:
            data = respo.json()
            return round(data['result'], 2)
        else:
            raise Exception('Erro')          
            