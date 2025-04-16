import ephem
from datetime import datetime
# numerology functions are defined below in this file
from human_design_utils import get_human_design_type

def get_astrology_data(name: str, birthdate: str, birthtime: str, birthlocation: str):
    try:
        # Parse date and time
        birth_dt = datetime.strptime(f"{birthdate} {birthtime}", "%Y-%m-%d %H:%M")
        observer = ephem.Observer()

        # Geocode manually for now (Replace with geocoder API or hardcoded input)
        # Example: London
        observer.lat, observer.lon = '51.5074', '-0.1278'
        observer.date = birth_dt

        # Get astro objects
        sun = ephem.Sun(observer)
        moon = ephem.Moon(observer)
        mercury = ephem.Mercury(observer)
        mars = ephem.Mars(observer)
        neptune = ephem.Neptune(observer)
        ascendant = observer.radec_of(0, 0)[0]  # Simplified ascendant stand-in

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
    # Abstract logic to assign your own signature descriptions
    # Astro values are reduced to signs/constellations in your brand system
    keys = {}

    # Placeholder brand-key mappings
    keys['Rooted Foundation'] = f"Signature for Mars: {astro_data.get('mars')}"
    keys['Heart of Connection'] = f"Signature for Moon: {astro_data.get('moon')}"
    keys['Self Expression'] = f"Signature for Sun: {astro_data.get('sun')}"
    keys['Mental Mastery'] = f"Signature for Mercury: {astro_data.get('mercury')}"
    keys['Awakened Self'] = f"Signature for Ascendant: {astro_data.get('ascendant')} + Neptune: {astro_data.get('neptune')}"

    # Add Numerology
    keys['Life Path Number'] = calculate_life_path(birthdate)
    keys['Destiny Number'] = calculate_destiny_number(name)
    
    return keys

