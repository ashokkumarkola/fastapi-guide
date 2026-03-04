from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def handle_email_username_integrity_error(e: IntegrityError):
    error = str(e.orig).lower()

    if "email" in error: # if "ix_users_email" in error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

    if "username" in error: # if "ix_users_username" in error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists"
        )

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Database integrity error"
    )

# handle_integrity_error()
# handle_foreign_key_error()
# handle_unique_constraint()
