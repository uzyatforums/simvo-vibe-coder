from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from request import get_animal_data

app = FastAPI(title="Vibe-Coder API")

@app.get("/hello")
async def read_hello():
    return {"message": "hello"}

app = FastAPI(title="Vibe-Coder API")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r") as f:
        return f.read()
    
@app.get("/species")
async def search_species(search: str):
    """
    Triggers the vibe-coder extraction logic.
    Example: /species?search=kangaroo
    """
    # Call the function from request.py and pass the query parameter
    data = get_animal_data(search)
    return data