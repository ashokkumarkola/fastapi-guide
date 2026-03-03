from pydantic import BaseModel

# ---- ERROR RESPONSE ---- #
class ErrorResponse(BaseModel):
    detail: str
