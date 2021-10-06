from ibackend import IBackend

class SheetsBackend(IBackend):

    def store_data(self, user_dto):
        # We're just printing out the data for now
        # to prove that we got here
        print('Sheets Backend received data: ')
        print(user_dto)