from fastapi import APIRouter, HTTPException
from backend.services.brawlstars import get_brawlers

# APIRouter groups related endpoints together.
# We'll register this router in main.py with a prefix of /brawlers.
router = APIRouter()

@router.get("/")
async def fetch_brawlers():
    try:
        brawlers_list = await get_brawlers()
        return brawlers_list

    except Exception as e:
        # If anything goes wrong (invalid tag, bad API key, network error),
        # return a clean error message instead of crashing.
        raise HTTPException(status_code=400, detail=str(e))
 