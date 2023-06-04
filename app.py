import os
from typing import List

from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/name")
def read_root():
    return {"name": "shani blau"}


@app.post("/uploadfile")
async def create_upload_file(files: List[UploadFile]):
    saved_files = []
    for file in files:
        name = file.filename
        if not os.path.exists("../dogs"):
            os.mkdir("../dogs")
        file_path = os.path.join("../dogs", name)
        with open(file_path, 'wb') as f:
            f.write(await file.read())
        saved_files.append(name)
    return {"filenames": saved_files}
