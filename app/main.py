from fastapi import FastAPI, HTTPException

from .schemas import HeightWorkSchema, HeightWorkSchemaCreate
from .db import create_height_works_in_db, get_height_works_from_db

app = FastAPI()


@app.post("/height-works", response_model=HeightWorkSchema)
async def create_height_work(height_work: HeightWorkSchemaCreate):
    new_hw: HeightWorkSchema = create_height_works_in_db(height_work)

    return new_hw


@app.get("/height-works/{id}", response_model=HeightWorkSchema)
async def get_height_work(id: int):
    try:
        found_hw: HeightWorkSchema = get_height_works_from_db(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=e.args[0])

    return found_hw
