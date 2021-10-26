from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException

from iscrapeservice import IScrapeService

class ProfScrapeService(IScrapeService):

    def scrape(self, user_dto):
        
        phone_number = user_dto.phone_number
        password = user_dto.password
        
        option = Options()
        option.add_argument('--disable-notifications')
        browser = webdriver.Chrome(options=option)
        browser.get('https://www.facebook.com/')

        phone_input = browser.find_element_by_name('email')
        password_input = browser.find_element_by_name('pass')
        login_button = browser.find_element_by_name('login')

        # # notice we are using username here but it will be phone number eventually
        phone_input.send_keys(phone_number)
        password_input.send_keys(password)
        login_button.click()

        time.sleep(2)

        browser.get("https://www.facebook.com/profile")

        time.sleep(5)
        
        def xpathWrapper(xpaths):
            for xpath in xpaths:
                try:
                    browser.find_element_by_xpath(xpath)
                except NoSuchElementException:
                    continue
                return browser.find_element_by_xpath(xpath)
            
            
        profNameXpaths = ['/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/span/h1', 
                          '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/h1']
        profName = xpathWrapper(profNameXpaths)
        
        #For some reason can't get direct svg xpaths, so have to go to parents, note, order of these xpaths 
        # matter since they both exist in the different web pages
        profPicXpaths = [
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div', 
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div']
        profPicHead = xpathWrapper(profPicXpaths)
        profPic = profPicHead.find_element_by_tag_name('image')

        user_dto.name = profName.text
        user_dto.prof_photo_url = profPic.get_attribute('xlink:href')

        browser.quit()


        


