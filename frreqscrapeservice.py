# This file is very heavily commented for instructional purposes. 
# We will get rid of these comments when they are no longer 
# necessary.

# Import the IScrapeServiceInterface
from iscrapeservice import IScrapeService

# This is how we create concrete classes from the IScraperService 
# interface (a Python Abstract Base Class).
class FrReqScrapeService(IScrapeService):

    # This method is required as part of the interface
    def scrape(self, user_dto):
        # The credentials will be passed in with the user_dto.
        # You can access the credentials like this:
        phone_number = user_dto.phone_number
        password = user_dto.password
        # This is where we will place the code that scrapes
        # the friend requests and puts them in the user_dto.
        user_dto.first_name = 'Drew' # delete me, I'm just an example
