# Brawl Stars Project

pinguiCookedYal tag: #2QUPCR9JO


# Build process
1. Set up the backend skeleton (FastAPI + .env)
2. Connect to the Brawl Stars API (fetch player data)
3. Build the calculation logic (gold/power math)
4. Build the frontend (search form + results display)
5. Connect frontend to backend

# First stage - Planning
What the flow will look like

  Browser (HTML/JS)  →  FastAPI (Python)  →  Brawl Stars API
                     ←  JSON response    ←  JSON response

  The browser never talks to Brawl Stars directly — FastAPI acts as the middleman and keeps your key hidden.

# Project Structure Plan
``` bash  
  Brawl_Stars_Project/
  ├── backend/
  │   ├── main.py              # FastAPI app — starts the server
  │   ├── config.py            # Loads the right .env based on APP_ENV
  │   ├── routes/
  │   │   └── player.py        # Endpoint: search player by tag
  │   ├── services/
  │   │   └── brawlstars.py    # Handles all calls to the Brawl Stars API
  │   ├── .env.dev             # Never committed
  │   ├── .env.prod            # Never committed
  │   └── .env.example         # Committed — safe template
  ├── frontend/
  │   ├── index.html           # Main (and only) page
  │   ├── css/
  │   │   └── style.css        # Custom styles
  │   └── js/
  │       └── main.js          # Fetches data from FastAPI, updates the UI
  ├── requirements.txt         # Python dependencies
  ├── .gitignore
  └── README.md
```

# How to run it
Step 1 - create the virtual environment inside the project folder
NOTE: A .venv keeps all the project dependencies isolated from your global Python installation. If you later work on another project with different package versions, they won't conflict.

1.1 Create venv
python -m venv .venv

1.2 Activate it

- On Windows (PowerShell):
.venv\Scripts\Activate.ps1
- On Windows (Command Prompt):
.venv\Scripts\activate.bat

NOTE: Once activated, your terminal will show (.venv) at the start of the line — that confirms you're inside the virtual environment. From that point, all pip install and python/uvicorn commands use the isolated environment.

Step 2 — install dependencies into the .venv:
pip install -r requirements.txt

Step 3 — add your API key to backend/.env.dev:
BRAWLSTARS_API_KEY=your_actual_key_here

Step 4 — start the server:
uvicorn backend.main:app --reload

Step 5 — test it in your browser or terminal:
GET http://localhost:8000/health
→ { "status": "ok", "env": "dev" }

Also, you may want to try http://localhost:8000/docs, so that you can test the API endpoints through Swagger.

