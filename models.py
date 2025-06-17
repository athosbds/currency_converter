import requests

class CurrencyConverter:
    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return round(amount, 2)
        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        respo =  requests.get(url)
        if respo.status_code == 200:
            data = respo.json()
            print(f'Resposta da API: {data}')
            rates = data.get('rates')     
            if rates and to_currency in rates:
                rate = rates[to_currency]
                return round(amount * rate, 2)
            else:
                raise Exception(f'Inválido')
        else:
            raise Exception(f'API não acessada.')
            