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

# This is how we create concrete classes from the IScraperService 
# interface (a Python Abstract Base Class).
class FriendScrapeService(IScrapeService):
    # This method is required as part of the interface
    def scrape(self, user_dto, browser):
        MAXIMUM_WAIT_TIME = 7 # maximum time to wait for necessary elements to appear, in seconds
        browser.implicitly_wait(MAXIMUM_WAIT_TIME)
        startTime = time.time()
        # Go to user's Facebook profile and wait for page to load
        browser.get("https://www.facebook.com/profile")
        friends_url = browser.current_url + "&sk=friends" # This is the url that represents their friends page
        browser.get(friends_url) # Go to their friends page

        
        friendNamesBeforeScrolling = None
        friendNamesAfterScrolling = []
        totalNumberOfFriends = None
        try:
            friendCountElement = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a")
            totalNumberOfFriends = int(friendCountElement.text.replace(" Friends", ""))
        except:
            print("Your thing broke.")
        print("Your total number of friends is: " + str(totalNumberOfFriends))
        while len(friendNamesAfterScrolling) < totalNumberOfFriends: # Let's just experiment, maybe there's 10 wonky friends that don't show up
            time.sleep(3) # By experimentation, I've found that this is a nice way to do it.
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            friendNamesAfterScrolling = browser.find_elements_by_xpath("//div[@class='buofh1pr hv4rvrfc']/div[1]/a/span")
            print(len(friendNamesAfterScrolling))

        friendNamesToPrint = []
        for friend in friendNamesAfterScrolling:
            friendNamesToPrint.append(friend.text)
        print(friendNamesToPrint)
        print(len(friendNamesToPrint))
        endTime = time.time()
        print("The total time for the friendsscraperservice to run is")
        print(endTime - startTime)
'''
        friendRequestPhotos = allFriends.find_elements_by_tag_name('image')
        friendRequestPhotosFinal = []
        for j in range(len(friendRequestPhotos)):
            if (friendRequestPhotos[j].get_attribute('style') == "height: 60px; width: 60px;"):
                friendRequestPhotosFinal.append(friendRequestPhotos[j].get_attribute('xlink:href'))
        
        # friendRequestPhotos = [a.get_attribute('xlink:href') for a in friendRequestPhotos]
        # print("Friend Request Photos = ")
        # print(friendRequestPhotosFinal)
        # #get the parent div of the 2 spans

        
        friendRequestNamesFinal = []
        friendRequestNames = allFriendRequests.find_elements_by_xpath("//span[contains(@class, 'lrazzd5p') and contains(@class, 'oo9gr5id')]")
        friendRequestNames = [name.text for name in friendRequestNames]
        for i in range(len(friendRequestNames)):
            # print("Name is = " + friendRequestNames[i])
            if friendRequestNames[i] == '' or friendRequestNames[i][:1].isdigit():
                pass
            else:
                friendRequestNamesFinal.append(friendRequestNames[i])

        # print(friendRequestNamesFinal)
        
        

        # # gets 2nd span's text and append to new array
        # for j in range(len(friendRequestNames)):
        #     tempArray = friendRequestNames[j].find_elements_by_tag_name('span')
        #     friendRequestNamesFinal.append(tempArray[1].text)

        # friendRequestPhotos = allFriendRequests.find_elements_by_tag_name('img')
        # friendRequestPhotos = [a.get_attribute('src') for a in friendRequestPhotos]

        user_dto.fr_name_list = friendRequestNamesFinal
        user_dto.fr_photo_list = friendRequestPhotosFinal
        '''