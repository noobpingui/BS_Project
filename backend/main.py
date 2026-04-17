from fastapi import FastAPI
from backend.config import APP_ENV
from backend.routes import player, brawlers

# Create the FastAPI application instance.
# This is the core object that handles all incoming HTTP requests.
app = FastAPI(
    title="Brawl Stars Stats API",
    description="Backend that proxies and processes Brawl Stars game data.",
    version="0.1.0"
)

# Register the player router under the /player prefix.
# All routes defined in player.py will be accessible under /player/...
app.include_router(player.router, prefix="/player")

# Register the brawlers router under the /brawlers prefix.
# All routes defined in brawlers.py will be accessible under /brawlers/...
app.include_router(brawlers.router, prefix="/brawlers")

# Health check endpoint.
# A simple route to confirm the server is running and show the active environment.
# Useful during deployment to verify everything started correctly.
@app.get("/health")
def health_check():
    return {"status": "ok", "env": APP_ENV}
