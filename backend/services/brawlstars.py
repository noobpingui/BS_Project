import httpx
from backend.config import BRAWLSTARS_API_KEY

# Base URL for all Brawl Stars API endpoints.
BASE_URL = "https://api.brawlstars.com/v1"

# Headers sent with every request to the Brawl Stars API.
# The Bearer token is how the API identifies and authorizes us.
HEADERS = {
    "Authorization": f"Bearer {BRAWLSTARS_API_KEY}"
}


async def get_player(tag: str) -> dict:
    """
    Fetch a player's profile from the Brawl Stars API by their tag.

    Tags start with '#' (e.g. #ABC123), but '#' is a reserved character
    in URLs, so we replace it with '%23' before sending the request.
    """

    # Encode the '#' in the tag so it's safe to use in a URL.
    encoded_tag = tag.upper().replace("#", "%23")

    # Use httpx as an async HTTP client.
    # 'async with' ensures the connection is properly closed after the request.
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/players/{encoded_tag}",
            headers=HEADERS
        )

        # Raise an exception automatically if the API returned an error
        # (e.g. 404 player not found, 403 invalid key).
        # This stops execution here and lets FastAPI handle the error response.
        response.raise_for_status()
        
        # Return the response body parsed as a Python dictionary.
        return response.json()
