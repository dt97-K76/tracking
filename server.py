from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json, os, datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/collect")
async def collect(request: Request):
    data = await request.json()

    os.makedirs("logs", exist_ok=True)

    filename = f"logs/{datetime.datetime.utcnow().isoformat()}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    return {"status": "ok"}
