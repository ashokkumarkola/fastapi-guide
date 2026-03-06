from phonenumbers import parse, is_valid_number, NumberParseException
from fastapi import HTTPException, status

"""
    ``- Only returns `True` or `False`.  
    - No HTTP exceptions here — keeps it reusable across contexts (Pydantic, CLI, service).
"""

def validate_phone(phone: str):
    try:
        number = parse(phone, None)
        return is_valid_number(number)
    except NumberParseException:
        # raise HTTPException(
        #     status_code=status.HTTP_400_BAD_REQUEST, 
        #     detail="Invalid phone number format"
        # )
        return False
