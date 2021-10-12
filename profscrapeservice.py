from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from iscrapeservice import IScrapeService

class ProfScrapeService(IScrapeService):

    def scrape(self, user_dto):
        
        phone_number = user_dto.phone_number
        password = user_dto.password
        
        # option = Options()
        # option.add_argument('--disable-notifications')
        # browser = webdriver.Chrome(options=option)
        # browser.get('https://www.facebook.com/')

        # phone_input = browser.find_element_by_name('email')
        # password_input = browser.find_element_by_name('pass')
        # login_button = browser.find_element_by_name('login')

        # # notice we are using username here but it will be phone number eventually
        # phone_input.send_keys(phone_number)
        # password_input.send_keys(password)
        # login_button.click()
        # time.sleep(2)
        # browser.quit()
        


