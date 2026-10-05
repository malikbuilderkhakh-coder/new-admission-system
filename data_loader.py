import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "admission_data.json"

def load_admission_data():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"notice": "No valid local admission dataset was found.", "programs": []}
