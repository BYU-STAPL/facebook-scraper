from ibackend import IBackend
from userprofilesheet import UserProfileSheet
from frsheet import FRSheet

class SheetsBackend(IBackend):

    def store_data(self, user_dto):
        self.sheets = [
            UserProfileSheet(),
            FRSheet()
        ]
        for sheet in self.sheets:
            sheet.store_data(user_dto)
