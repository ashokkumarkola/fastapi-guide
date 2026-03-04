import os
import shutil
from uuid import uuid4
from fastapi import UploadFile

# from app.core.config import get_settings

# settings = get_settings()



class FileUploadUtil:

    @staticmethod
    def save_image(image: UploadFile, upload_dir: str) -> str:
        os.makedirs(upload_dir, exist_ok=True)

        image_name = f"{uuid4()}_{image.filename}"
        image_path = os.path.join(upload_dir, image_name)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        return image_path