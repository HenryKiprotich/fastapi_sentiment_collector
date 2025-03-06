
from fastapi import APIRouter, HTTPException
from models import SentimentData
from database import collection
from typing import List  # Import List

router = APIRouter(prefix="/collect", tags=["collector"])

@router.post("/insert")
async def insert_data(data: List[SentimentData]):  # Accepts a list of SentimentData
    documents = [entry.dict() for entry in data]  # Convert Pydantic objects to dictionaries
    result = await collection.insert_many(documents)  # Use insert_many instead of insert_one
    if result.inserted_ids:
        return {"message": "Data inserted successfully", "ids": [str(id) for id in result.inserted_ids]}
    raise HTTPException(status_code=500, detail="Data insertion failed")
