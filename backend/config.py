import os
from pathlib import Path
from dotenv import load_dotenv

# Determine which environment we're running in.
# APP_ENV must be set before starting the server (e.g. APP_ENV=dev uvicorn ...).
# Defaults to "dev" if not set, so local development works out of the box.
APP_ENV = os.getenv("APP_ENV", "dev")

# Build the path to the matching .env file (e.g. backend/.env.dev).
# Path(__file__).parent points to the backend/ folder regardless of where
# the server is launched from — this makes the path always reliable.
env_file = Path(__file__).parent / f".env.{APP_ENV}"

# Load the environment variables from the file into os.environ.
load_dotenv(env_file)

# Expose the API key so other modules can import it from config.
# If the key is missing, we raise an error immediately so the problem
# is obvious at startup rather than failing silently on the first request.
BRAWLSTARS_API_KEY = os.getenv("BRAWLSTARS_API_KEY")
if not BRAWLSTARS_API_KEY:
    raise EnvironmentError(
        f"BRAWLSTARS_API_KEY is not set. "
        f"Check your backend/.env.{APP_ENV} file."
    )
