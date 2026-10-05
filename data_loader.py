import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "admission_data.json"

def load_admission_data():
    """Load the small starter dataset. This is illustrative, not a live database."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "notice": "No local dataset found. Treat all institution-specific requirements as unverified.",
            "programs": [],
        }
    except json.JSONDecodeError:
        return {
            "notice": "Admission dataset could not be read. Treat institution-specific requirements as unverified.",
            "programs": [],
        }
