from userdto import UserDTO

class Scraper():

    def __init__(self, phone_number, password):
        self.scrape_services = []
        self.user_dto = UserDTO(phone_number, password, None, None)

    def scrape(self):
        for service in self.scrape_services:
            service.scrape(self.user_dto)

    def attach(self, scrape_service):
        self.scrape_services.append(scrape_service)