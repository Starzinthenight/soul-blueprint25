from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from blueprint_utils import get_astrology_data, get_blueprint_keys

app = FastAPI()

# ✅ CORS middleware to allow only your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.soulaligned.life"],  # Your exact frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Data model matching your frontend
class UserData(BaseModel):
    name: str
    email: str
    birthdate: str      # Format: YYYY-MM-DD
    birthtime: str      # Format: HH:MM
    birthplace: str
    latitude: float
    longitude: float

# ✅ Blueprint generation endpoint
@app.post("/soul-blueprint")
async def generate_blueprint(user: UserData):
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

    blueprint = get_blueprint_keys(
        astro_data=astro_data,
        name=user.name,
        birthdate=user.birthdate
    )

    return {
        "status": "success",
        "name": user.name,
        "life_path_number": blueprint.get("Life Path Number"),
        "destiny_number": blueprint.get("Destiny Number"),
        "summary": blueprint.get("Soul Summary", "Your unique blueprint is ready."),
        "unlocked_modules": blueprint.get("Unlocked Modules", [])
    }

# ✅ Root route to check if API is live
@app.get("/")
def read_root():
    return {"message": "Soul Blueprint API is running!"}

# ✅ Version check to verify correct code is deployed
@app.get("/version-check")
def version_check():
    return {"version": "1.0.3", "message": "CORS-enabled backend is live"}
