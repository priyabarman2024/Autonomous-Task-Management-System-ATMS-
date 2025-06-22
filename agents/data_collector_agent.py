import requests
from bs4 import BeautifulSoup

class DataCollectorAgent:
    def __init__(self):
        pass

    def collect_data(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('p')  # Extracts paragraph text, for example
        return [item.text for item in data]
