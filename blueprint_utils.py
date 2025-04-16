import ephem
from datetime import datetime
from numerology import calculate_life_path, calculate_destiny_number
from hd_utils import get_human_design_type


def get_astrology_data(name: str, birthdate: str, birthtime: str, birthlocation: str,
                       latitude: float, longitude: float):
    try:
        # Convert birth datetime
        birth_dt = datetime.strptime(f"{birthdate} {birthtime}", "%Y-%m-%d %H:%M")

        # Setup ephem observer
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.lon = str(longitude)
        observer.date = birth_dt

        # Compute celestial body positions
        sun = ephem.Sun(observer)
        moon = ephem.Moon(observer)
        mercury = ephem.Mercury(observer)
        mars = ephem.Mars(observer)
        neptune = ephem.Neptune(observer)
        ascendant = observer.radec_of(0, 0)[0]  # Simplified ascendant approximation

        return {
            "sun": sun.ra,
            "moon": moon.ra,
            "mercury": mercury.ra,
            "mars": mars.ra,
            "neptune": neptune.ra,
            "ascendant": ascendant
        }

    except Exception as e:
        return {"error": f"Astrology calculation failed: {str(e)}"}


def get_blueprint_keys(astro_data, name, birthdate):
    # Abstract brand-aligned output: no zodiac names, just signature placeholders
    keys = {}

    # Brand-aligned module interpretations (based on your Star Steps)
    keys['Root – Security'] = f"Signature match: Mars alignment → {astro_data.get('mars')}"
    keys['Heart – Connection'] = f"Signature match: Moon alignment → {astro_data.get('moon')}"
    keys['Sacral – Expression'] = f"Signature match: Sun alignment → {astro_data.get('sun')}"
    keys['Crown – Mental Mastery'] = f"Signature match: Mercury alignment → {astro_data.get('mercury')}"
    keys['Soul Star – Self-Awakening'] = f"Signature match: Ascendant + Neptune → {astro_data.get('ascendant')} + {astro_data.get('neptune')}"

    # Numerology
    keys['Life Path Number'] = calculate_life_path(birthdate)
    keys['Destiny Number'] = calculate_destiny_number(name)

    # Human Design (optional, fallback-safe)
    try:
        hd_type = get_human_design_type(birthdate, birthtime=None, name=name)
        keys['Human Design Type'] = hd_type
    except Exception:
        keys['Human Design Type'] = "Unavailable"

    # Summary logic — can be custom or stitched from the signatures
    keys['Soul Summary'] = f"Your unique design is a fusion of cosmic alignments and archetypal energies aligned with your Soul Blueprint."

    # Unlocked Modules (used in frontend color display)
    keys['Unlocked Modules'] = [
        "Root – Security",
        "Heart – Connection",
        "Sacral – Expression",
        "Crown – Mental Mastery",
        "Soul Star – Self-Awakening"
    ]

    return keys
