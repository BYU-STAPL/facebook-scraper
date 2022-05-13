from userdto import UserDTO
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import os

class Scraper():

    def __init__(self, phone_number, password):
        self.backend = None
        self.scrape_services = []
        self.user_dto = UserDTO(phone_number, password, None, None, None, None)

    def scrape(self):
        username = self.user_dto.phone_number
        password = self.user_dto.password
        
        # disabling notification popups
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        browser.get('https://www.facebook.com/')
         
        phone_input = browser.find_element_by_name('email')
        password_input = browser.find_element_by_name('pass')
        login_button = browser.find_element_by_name('login')

        # notice we are using username here but it will be phone number eventually
        phone_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        # wait 3 seconds if needed
        browser.implicitly_wait(3)
        
        for service in self.scrape_services:
            service.scrape(self.user_dto, browser)
        
        self.backend.store_data(self.user_dto)
        browser.quit()

    def attach_scraper(self, scrape_service):
        self.scrape_services.append(scrape_service)

    def attach_backend(self, backend):
        self.backend = backend
