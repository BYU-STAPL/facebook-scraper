from dataclasses import dataclass

@dataclass
class UserDTO:
    phone_number: str
    password: str
    first_name: str
    last_name: str