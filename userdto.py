from dataclasses import dataclass

@dataclass
class UserDTO:
    phone_number: str
    password: str
    first_name: str
    last_name: str
    fr_name_list: str
    fr_photo_list: str