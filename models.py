import requests

class CurrencyConverter:
    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return round(amount, 2)
        url = url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"

        respo =  requests.get(url)
        if respo.status_code == 200:
            data = respo.json()
            print(f'Resposta da API: {data}')     
            if data.get('success') and 'result' in data:
                return round(data['result'], 2)
            else:
                raise Exception(f'Inválido')
        else:
            raise Exception(f'API não acessada.')
            