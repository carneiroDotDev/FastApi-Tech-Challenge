# python3 -m venv NanoTemper
# pip3 install -r requirements.txt
# uvicorn server.main:app --reload
# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
import pandas as pd

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile, status, HTTPException
from typing import Optional

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
async def main():
    content = """
<body>
<form action="/findmax/" enctype="multipart/form-data" method="post">
<input name="file" type="file" required>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.post("/findmax/", status_code=status.HTTP_200_OK)
# One may arguee that positive status should be 201. Up to discussion.
async def maxFinder(file: UploadFile = File(...), separator: Optional[str] = ";"):
    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="CSV file not found")

    if ".csv" not in file.filename:
        raise HTTPException(
            status_code=status.HTTP_411_LENGTH_REQUIRED, detail="File extension is not .csv")

    try:
        df = pd.read_csv(file.file, encoding='utf-8', sep=separator)
        maxFreq = df['frequency'].max()
        maxValues = df[df['frequency'] == maxFreq]
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad file format. Considered .csv with {separator} as separator and two columns (Radius and Frequency).")

    return maxValues
