ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
WEB_FILE = "web_file.html"

class Scrape:
    def __init__(self):
        super().__init__()
        self.link_list = []
        self.price_list = []
        self.address_list = []

    def read_web_file(self):
        """
        If web file does not exist, then retrive web page\n
        Open web file and return a BeautifulSoup object (HTML
        :return: nothing
        """
        from bs4 import BeautifulSoup

        try:
            open(WEB_FILE)
        except FileNotFoundError:
            self.get_page()
        else:
            pass
        finally:
            # Read the web page from file
            with open(WEB_FILE, mode='r', encoding='utf-8') as fp:
                content = fp.read()
        return BeautifulSoup(content, 'html.parser')

    def get_page(self):
        """
        Retrieve requested web page\n
        Render in browser to execute the page's JavaScript\n
        Save the rendered web page to a file
        """
        from selenium import webdriver

        chrome_driver_path = "/opt/WebDriver/chromedriver"
        driver = webdriver.Chrome(executable_path=chrome_driver_path)

        driver.get(ZILLOW_URL)

        go = input("Allow the page to complete render in the browser.\n Enter Y to save the web page! ").lower()
        if go == "y":
            html_source = driver.page_source
            # Save web page to file
            with open(WEB_FILE, mode='w', encoding='utf-8') as fp:
                fp.write(html_source)

    def list_links(self, soup):
        # Create a list of links from zillow
        links = soup.find_all(class_="list-card-info")
        for l in links:
            try:
                link = l.find('a', class_='list-card-link')['href']
                if 'https' not in link:
                    link = f"https://www.zillow.com" + link
            except TypeError:
                continue
            self.link_list.append(link)
        print(len(self.link_list))
        print(self.link_list)
        return self.link_list

    def list_prices(self, soup):
        # Create a list of prices from zillow
        prices = soup.find_all(class_='list-card-price')
        self.price_list = [price.get_text().split('/')[0].split('+')[0] for price in prices]
        print(len(self.price_list))
        print(self.price_list)
        return self.price_list

    def list_addresses(self, soup):
        # Create a list of addresses from zillow
        addresses = soup.find_all(class_='list-card-addr')
        for address in addresses:
            split = address.get_text().split("|")
            if len(split) < 2:
                self.address_list.append(split[0])
            else:
                self.address_list.append(split[1])
        print(self.address_list)
        return self.address_list
