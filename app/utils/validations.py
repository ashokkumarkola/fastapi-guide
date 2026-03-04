import phonenumbers
from phonenumbers import NumberParseException

def validate_phone(phone: str):
    try:
        number = phonenumbers.parse(phone, None)
        return phonenumbers.is_valid_number(number)
    except NumberParseException:
        return False
