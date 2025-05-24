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