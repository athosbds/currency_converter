import requests

class CurrencyConverter:
    def __init__(self, api_urls):
        self.api_urls = api_urls
        self.rates = {}
    def fetch_rates(self):
        """
        Aqui busca as taxas de câmbio apartir das 
        URL Api presentes app.py"""
        for currency, url in self.api_urls.items():
            response = requests.get(url)
            if response.status_code == 200:
                self.rates[currency] = response.json().get('rates', {})
            else:
                raise Exception(f'Error fethcing {currency}')  
    def convert(self, amount, from_currency, to_currency):
        """Conversões utilizando o Dólar americano"""
        if from_currency == to_currency:
                return round(amount, 2)
        try:
            from_rates = self.rates[from_currency]
            if to_currency not in from_rates:
                raise Exception('Conversão não suportada')
            converted_amount =  amount * from_rates[to_currency] 
            return round(converted_amount, 2)
        except KeyError:
            raise Exception('Moeda não suportada')           
            