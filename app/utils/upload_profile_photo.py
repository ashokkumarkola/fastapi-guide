# import os
# import shutil
# from uuid import uuid4
# from fastapi import UploadFile, HTTPException
# from app.core.config import get_settings

# settings = get_settings()
# BASE_UPLOAD_DIR = settings.BASE_UPLOAD_DIR


# def save_upload_file(
#     file: UploadFile,
#     folder: str,
#     allowed_types: list[str] | None = None,
# ) -> str:
#     """
#     Save uploaded file locally and return public URL.
#     """

#     # Validate content type
#     if allowed_types and file.content_type not in allowed_types:
#         raise HTTPException(status_code=400, detail="Invalid file type")

#     # Create folder
#     upload_path = os.path.join(BASE_UPLOAD_DIR, folder)
#     os.makedirs(upload_path, exist_ok=True)

#     # Generate unique filename
#     extension = file.filename.split(".")[-1]
#     filename = f"{uuid4()}.{extension}"

#     file_path = os.path.join(upload_path, filename)

#     # Save file
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # Return URL path (not filesystem path)
#     return f"/uploads/{folder}/{filename}"