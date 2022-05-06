from dataclasses import dataclass

@dataclass
class UserDTO:
    phone_number: str
    password: str
    name: str
    fr_name_list: str
    fr_photo_list: str
    prof_photo_url: str