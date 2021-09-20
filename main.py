# This file shows an example of how the system can be used.
# I think this should provide lots of flexibility for 
# different studies.

# Import the scraper and the scraper services required
# for the given study.
from scraper import Scraper
from frreqscrapeservice import FrReqScrapeService

# Initialize the scraper with the credentials for the
# study participant (one-time passwords only!!!)
scraper = Scraper('8888888888', 'fakePassword')

# Attach the scrape services you'll be using.
scraper.attach(FrReqScrapeService())

# Call scrape to gather all data
scraper.scrape()

print(scraper.user_dto)