# This class is responsible for get all the friends associated with a certain event on Facebook.
# It scrapes recent events as well as some of the friends that went to those recent events


import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import the IScrapeServiceInterface
from .iscrapeservice import IScrapeService

class EventFriendsScrapeService(IScrapeService):
    def scrape(self, user_dto, browser):
        MAXIMUM_WAIT_TIME = 7 # maximum time to wait for necessary elements to appear, in seconds
        browser.implicitly_wait(MAXIMUM_WAIT_TIME)
        browser.get("https://www.facebook.com/events/")

        # Click the Create new event button:
        browser.find_element(By.XPATH, "//span[text()='Create new event'").click()