import requests

class CurrencyConverter:
    def __init__(self, api_urls):
        self.api_urls = api_urls
        self.rates = {}
    def fetch_rates(self):
        for currency, url in self.api_urls:
            response = requests.get(url)
            if response.status_code == 200:
                self.rates[currency] = response.json().get('rate', {})
            else:
                raise Exception(f'Error fethcing {currency}')  
    def converter(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        if from_currency == 'USD':
            base_amount = amount
        else:
            base_amount = amount / self.rates['USD'].get(from_currency, 1)
        if to_currency == 'USD':
            return base_amount
        return base_amount * self.rates['USD'].get(to_currency, 1)