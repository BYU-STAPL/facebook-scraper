from ibackend import IBackend
from userprofilesheet import UserProfileSheet
from frsheet import FRSheet
from fakeDataFRSheet import FakeDataFRSheet

class SheetsBackend(IBackend):
    def __init__(self, keysName, spreadsheetId):
        self.keys = keysName
        self.spreadsheetId = spreadsheetId
    
    def store_data(self, user_dto):
        self.sheets = [
            UserProfileSheet(self.keys, self.spreadsheetId),
            # FRSheet(self.keys, self.spreadsheetId)
            FRSheet(self.keys, self.spreadsheetId)
        ]
        for sheet in self.sheets:
            sheet.store_data(user_dto)
