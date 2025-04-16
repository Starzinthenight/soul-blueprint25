from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from blueprint_utils import get_astrology_data, get_blueprint_keys

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to soulaligned.life in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserData(BaseModel):
    name: str
    email: str
    birthdate: str  # format: YYYY-MM-DD
    birthtime: str  # format: HH:MM
    birthplace: str  # Placeholder for location logic

@app.post("/generate-blueprint")
async def generate_blueprint(user: UserData):
    # Step 1: Get raw data
    astro_data = get_astrology_data(
        name=user.name,
        birthdate=user.birthdate,
        birthtime=user.birthtime,
        birthlocation=user.birthplace
    )

    if "error" in astro_data:
        return {"status": "error", "message": astro_data["error"]}

    # Step 2: Get branded output
    blueprint = get_blueprint_keys(
        astro_data=astro_data,
        name=user.name,
        birthdate=user.birthdate
    )

    # Step 3: Return JSON (or trigger PDF/email logic here)
    return {"status": "success", "blueprint": blueprint}

