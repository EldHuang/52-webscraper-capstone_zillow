import requests
from bs4 import BeautifulSoup

class Zillow:
    def __init__(self):
        url = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
        self.soup = BeautifulSoup(url.text, "html.parser")

    def address(self):
        addr_list = self.soup.find_all("address")
        addr_list = [
            item.text.split("|")[-1].strip() if "|" in item.text
            else item.text.split(",", 1)[-1].strip()
            for item in addr_list
        ]
        return addr_list

    def link(self):
        links = self.soup.find_all("a", attrs={"data-test": "property-card-link"})
        links = list(dict.fromkeys([link.get("href") for link in links]))
        return links

    def price(self):
        prices = [price.text.strip() for price in self.soup.find_all("span", attrs={"data-test": "property-card-price"})]
        prices = [
            price.split("+")[0] if "+" in price
            else price.split("/")[0]
            for price in prices
        ]
        return prices