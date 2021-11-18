from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from isheet import ISheet

class FakeDataFRSheet(ISheet):
    def __init__(self, keysName, spreadsheetId):
        self.keys = keysName
        self.spreadsheetId = spreadsheetId

    def store_data(self, user_dto):
        # Credentials
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = self.keys
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        #Sheet Manipulation
        SPREADSHEET_ID = self.spreadsheetId
        
        #Fake Data
        fakeFrNames = ['Julia Hampton',
                       'Josefina Kolakovic',
                       'Woodie Wasbrough',
                       'Niki Penhaleurack',
                       'Brenden Overland',
                       'Elena Kearn',
                       'Moses Ferraretto',
                       'Mandi Crus',
                       'Gavan Oven',
                       'Sianna Donohoe',
                       'Clark Lashmar',
                       'Susan Ciciotti',
                       'Sherlock Helstrom',
                       'Emma Roumier',
                       'Shaun Champerlen',
                       'Sophia Bratt']
        fakeFrPhotos = ['https://images.unsplash.com/photo-1520635360276-79f3dbd809f6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1180&q=80', 
                        'https://images.unsplash.com/photo-1522228115018-d838bcce5c3a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1524666041070-9d87656c25bb?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1506956191951-7a88da4435e5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1674&q=80',
                        'https://images.unsplash.com/photo-1480455624313-e29b44bbfde1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1770&q=80',
                        'https://images.unsplash.com/photo-1594744803329-e58b31de8bf5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1558487661-9d4f01e2ad64?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1534751516642-a1af1ef26a56?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=778&q=80',
                        'https://images.unsplash.com/photo-1519058082700-08a0b56da9b4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1512503868941-bd9fa9c6b569?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1770&q=80',
                        'https://images.unsplash.com/photo-1508341591423-4347099e1f19?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1512968067576-4d0b04f58130?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1543084951-1650d1468e2d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1513102464262-e2ef5a4b1a5b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=814&q=80',
                        'https://images.unsplash.com/photo-1514461713809-b245d3816ff1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=774&q=80',
                        'https://images.unsplash.com/photo-1440178536296-c1041e136dda?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1770&q=80']

        newFrNames = user_dto.fr_name_list
        newFrPhotos = user_dto.fr_photo_list
        # diffFr = len(fakeFrNames) - len(user_dto.fr_name_list)
        #Sets every other to fake data
        for i in range(len(user_dto.fr_name_list)):
            if (i%2 == 1):
                newFrNames[i] = fakeFrNames.pop(0)
                newFrPhotos[i] = fakeFrPhotos.pop(0)
        
        #Sets remaining fake data into array
        while (len(newFrNames) < 15):
            newFrNames.append(fakeFrNames.pop(0))
            newFrPhotos.append(fakeFrPhotos.pop(0))
            
        
        service = build('sheets', 'v4', credentials=creds)

        column_names = [('Name', 'ProfilePhoto')]
        data = list(zip(newFrNames, newFrPhotos))

        values = column_names + data

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range="FriendRequests!A1:B100",
            valueInputOption = "USER_ENTERED",
            body=body).execute()
        print('{0} cells updated.'.format(result.get('updatedCells')))

