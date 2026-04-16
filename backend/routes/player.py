from fastapi import APIRouter, HTTPException
from backend.services.brawlstars import get_player

# APIRouter groups related endpoints together.
# We'll register this router in main.py with a prefix of /player.
router = APIRouter()


@router.get("/{tag}")
async def fetch_player(tag: str):
    """
    GET /player/{tag}

    Receives a player tag from the URL, fetches the player's profile
    from the Brawl Stars API, and returns it as JSON.
    """
    try:
        player = await get_player(tag)
        return player

    except Exception as e:
        # If anything goes wrong (invalid tag, bad API key, network error),
        # return a clean error message instead of crashing.
        raise HTTPException(status_code=400, detail=str(e))
