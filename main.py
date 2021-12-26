from scrape import Scrape
from form import Form

scrape = Scrape()
form = Form()
soup = scrape.read_web_file()

links = scrape.list_links(soup)
prices = scrape.list_prices(soup)
addresses = scrape.list_addresses(soup)

form.fill_in_form(links, prices, addresses)
