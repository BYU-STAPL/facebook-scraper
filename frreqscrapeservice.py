# This file is very heavily commented for instructional purposes. 
# We will get rid of these comments when they are no longer 
# necessary.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# export PHONE="100061986225169"
# export FB_PWD="12Password34"

# Import the IScrapeServiceInterface
from iscrapeservice import IScrapeService

# This is how we create concrete classes from the IScraperService 
# interface (a Python Abstract Base Class).
class FrReqScrapeService(IScrapeService):

    # This method is required as part of the interface
    def scrape(self, user_dto):
        # The credentials will be passed in with the user_dto.
        # You can access the credentials like this:
        username = user_dto.phone_number
        password = user_dto.password
        
        # disabling notification popups
        option = Options()
        option.add_argument('--disable-notifications')
        browser = webdriver.Chrome(options=option)
        browser.get('https://www.facebook.com/')

        phone_input = browser.find_element_by_name('email')
        password_input = browser.find_element_by_name('pass')
        login_button = browser.find_element_by_name('login')

        # notice we are using username here but it will be phone number eventually
        phone_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        time.sleep(3)
        
        browser.get("https://www.facebook.com/friends")
        time.sleep(3)
        
        seeMore = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]')
        seeMore.click()
        time.sleep(3)
        
        allFriendRequests = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div')

        #get the parent div of the 2 spans
        friendRequestNames = allFriendRequests.find_elements_by_xpath("//div[contains(@class, 'tvmbv18p') and contains(@class, 'aahdfvyu')]")

        friendRequestNamesFinal = []

        # gets 2nd span's text and append to new array
        for j in range(len(friendRequestNames)):
            tempArray = friendRequestNames[j].find_elements_by_tag_name('span')
            friendRequestNamesFinal.append(tempArray[1].text)

        friendRequestPhotos = allFriendRequests.find_elements_by_tag_name('img')
        friendRequestPhotos = [a.get_attribute('src') for a in friendRequestPhotos]

        user_dto.fr_name_list = friendRequestNamesFinal
        user_dto.fr_photo_list = friendRequestPhotos
        
        # print("All finished fr scrape")
        browser.quit()