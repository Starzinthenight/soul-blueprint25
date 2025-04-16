from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from blueprint_utils import get_astrology_data, get_blueprint_keys

app = FastAPI()

# CORS: allow frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.soulaligned.life"],  # ← only allow your live site
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic data model
class UserData(BaseModel):
    name: str
    email: str
    birthdate: str  # format: YYYY-MM-DD
    birthtime: str  # format: HH:MM
    birthplace: str
    latitude: float
    longitude: float

# POST endpoint
@app.post("/soul-blueprint")
async def generate_blueprint(user: UserData):
    # Step 1: Get raw astrology & numerology data
    astro_data = get_astrology_data(
        name=user.name,
        birthdate=user.birthdate,
        birthtime=user.birthtime,
        birthlocation=user.birthplace,
        latitude=user.latitude,
        longitude=user.longitude
    )

    if "error" in astro_data:
        return {"status": "error", "message": astro_data["error"]}

    # Step 2: Get blueprint keys based on your branding
    blueprint = get_blueprint_keys(
        astro_data=astro_data,
        name=user.name,
        birthdate=user.birthdate
    )

    # Step 3: Return final response to frontend
    return {
        "status": "success",
        "name": user.name,
        "life_path_number": blueprint.get("Life Path Number"),
        "destiny_number": blueprint.get("Destiny Number"),
        "summary": blueprint.get("Soul Summary", "Your unique blueprint is ready."),
        "unlocked_modules": blueprint.get("Unlocked Modules", [])
    }

# Optional root route to confirm service is alive
@app.get("/")
def read_root():
    return {"message": "Soul Blueprint API is running!"}
