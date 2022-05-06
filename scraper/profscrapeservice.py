from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from iscrapeservice import IScrapeService

class ProfScrapeService(IScrapeService):

    def scrape(self, user_dto, browser):
        browser.get("https://www.facebook.com/profile")

        time.sleep(5)
        
        def xpathWrapper(xpaths):
            for xpath in xpaths:
                try:
                    browser.find_element(By.XPATH, xpath)
                except NoSuchElementException:
                    continue
                return browser.find_element(By.XPATH, xpath)
            
        
        profNameXpaths = ['/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/div/h1']
        profName = xpathWrapper(profNameXpaths)
    
        
        #For some reason can't get direct svg xpaths, so have to go to parents, note, order of these xpaths 
        # matter since they both exist in the different web pages
        profPicXpaths = [
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div', 
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div']
        profPicHead = xpathWrapper(profPicXpaths)
        profPic = profPicHead.find_element(By.TAG_NAME, 'image')

        user_dto.name = profName.text
        user_dto.prof_photo_url = profPic.get_attribute('xlink:href')



        


