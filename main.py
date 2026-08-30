from zillow import Zillow
from forms import Forms

soup = Zillow()
locations = soup.address()
cost = soup.price()
links = soup.link()

form = Forms()
form.fill_form(addr_list=locations, price_list=cost, links_list=links)