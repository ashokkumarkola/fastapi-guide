from fastapi import FastAPI, Request, HTTPException, status
from ..constants import PRODUCT_NOT_FOUND

from fastapi.responses import JSONResponse

def product_not_found():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=PRODUCT_NOT_FOUND
        # headers={"X-Error": "There goes my error"},
    )


# Return vs Raise

# it won't run the rest of the code in the path operation function, 
# it will terminate that request right away and send the HTTP error from the HTTPException to the client


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# @app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

#  raise UnicornException(name=name)
