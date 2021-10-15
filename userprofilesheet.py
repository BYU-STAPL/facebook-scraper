from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

from isheet import ISheet

class UserProfileSheet(ISheet):

    def store_data(self, user_dto):
        # Credentials
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        #Sheet Manipulation
        # The ID and range of a sample spreadsheet.
        SPREADSHEET_ID = '1oFPY4kaiqCih2FULkxqkjy8XbO5Vbya3HQku4w8Ys1g'

        service = build('sheets', 'v4', credentials=creds)

        values = [
            [
                'Name', 'ProfilePhoto'
            ],
            [
                user_dto.name, user_dto.prof_photo_url
            ]
        ]

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range="UserProfile!A1:B2",
            valueInputOption = "USER_ENTERED",
            body=body).execute()
        print('{0} cells updated.'.format(result.get('updatedCells')))





