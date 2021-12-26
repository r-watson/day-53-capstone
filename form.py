
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfEsGoQdHU4W4n67O7wxGIGBUqDKH9Tz9iHJUpvXTLcGRMPaw/viewform?usp=sf_link"


class Form:

    def fill_in_form(self, links, prices, addresses):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys

        # open google form to input data from scraped zillow search
        chrome_driver_path = "/opt/WebDriver/chromedriver"
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get(GOOGLE_FORM)

        time.sleep(2)

        for i in range(len(addresses)):
            # fill in address field
            addr_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            addr_field.send_keys(addresses[i])

            # fill in price field
            price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field.send_keys(prices[i])

            # fill in link field
            link_field = driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field.send_keys(links[i])

            # click submit button
            submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()

            # click submit another response link
            submit_another = driver.find_element(By.LINK_TEXT, 'Submit another response')
            submit_another.click()

            time.sleep(2)

