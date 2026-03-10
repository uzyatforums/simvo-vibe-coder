from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware  # Required for browser requests
from request import get_animal_data

app = FastAPI(title="Vibe-Coder API")

# --- CORS Configuration ---
# This allows your HTML file to talk to the API without being blocked
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, etc.
    allow_headers=["*"],
)

@app.get("/hello")
async def read_hello():
    return {"message": "hello"}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Ensure your index.html is inside a 'templates' folder
    with open("templates/index.html", "r") as f:
        return f.read()
    
@app.get("/species")
async def search_species(search: str):
    """
    Triggers the vibe-coder extraction logic.
    Example: /species?search=kangaroo
    """
    data = get_animal_data(search)
    return data