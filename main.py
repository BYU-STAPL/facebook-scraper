from getpass import getpass, getuser

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

scraper = Scraper(input('Username/Phone: '), getpass())

# Set the backend with the name of the keys file and spreadsheet ID
def createGoogleSheetsBackend():
    keyName = 'keys.json'
    spreadsheetID = '1GtLupC4bNrhngFSY3ToihvZxmMTwobMl6GF-9KwjjRY'
    backend = SheetsBackend(keyName, spreadsheetID)
    # attach the sheets to this backend
    from userprofilesheet import UserProfileSheet
    from frsheet import FRSheet
    from fakeDataFRSheet import FakeDataFRSheet
    backend.add_sheet(UserProfileSheet(keyName, spreadsheetID))
    backend.add_sheet(FRSheet(keyName, spreadsheetID))
    return backend

# attach the backend to the scraper
scraper.attach_backend(createGoogleSheetsBackend())
# Attach the scrape services you'll be using.
scraper.attach_scraper(FrReqScrapeService())
scraper.attach_scraper(ProfScrapeService())

# Call scrape to gather all data
scraper.scrape()