import string
from enum import Enum

class CheckType(Enum):
    LOWER = 1
    SPECIAL = 2

def check_password(type: CheckType, minLenght: int, password: str):
    if(type == CheckType.LOWER):
        if(len(password) >= minLenght and any(char.islower() for char in password)):
            return True
        
    elif(type == CheckType.SPECIAL):
        specialChar = string.punctuation
        if(len(password) >= minLenght and any(char in specialChar for char in password)):
            return True
        
    else:
        raise ValueError("Error CheckType")
        
password = "Hello%World123"

print(check_password(CheckType.LOWER, 4, password) and check_password(CheckType.SPECIAL, 2, password))

