from getpass import getpass, getuser
import sys
import os
import json

# This file shows an example of how the system can be used.
# I think this should provide lots of flexibility for 
# different studies.

# Import the scraper and the scraper services required
# for the given study.
from scraper import Scraper
from frreqscrapeservice import FrReqScrapeService
from profscrapeservice import ProfScrapeService
from sheetsbackend import SheetsBackend

# Initialize the scraper with the credentials for the
# study participant (one-time passwords only!!!)
# Here, we read the credentials from env vars so that creds
# aren't being pushed to the public repo

username = sys.argv[1]
password = sys.argv[2]

scraper = Scraper(username, password)
# scraper = Scraper(input('Username/Phone: '), getpass())

# Set the backend with the name of the keys file and spreadsheet ID
def createGoogleSheetsBackend():
    account_info = json.loads(os.environ.get("KEYS_JSON"))
    spreadsheetID = '1GtLupC4bNrhngFSY3ToihvZxmMTwobMl6GF-9KwjjRY'
    backend = SheetsBackend(account_info, spreadsheetID)
    # attach the sheets to this backend
    from userprofilesheet import UserProfileSheet
    from frsheet import FRSheet
    from fakeDataFRSheet import FakeDataFRSheet
    backend.add_sheet(UserProfileSheet(account_info, spreadsheetID))
    backend.add_sheet(FRSheet(account_info, spreadsheetID))
    return backend

# attach the backend to the scraper
scraper.attach_backend(createGoogleSheetsBackend())
# Attach the scrape services you'll be using.
scraper.attach_scraper(FrReqScrapeService())
scraper.attach_scraper(ProfScrapeService())

# Call scrape to gather all data
scraper.scrape()