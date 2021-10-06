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
import os
scraper = Scraper(os.environ['PHONE'], os.environ['FB_PWD'])

# Set the backend 
scraper.attach_backend(SheetsBackend())

# Attach the scrape services you'll be using.
scraper.attach_scraper(FrReqScrapeService())
scraper.attach_scraper(ProfScrapeService())

# Call scrape to gather all data
scraper.scrape()