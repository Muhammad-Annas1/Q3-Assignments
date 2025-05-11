import os
import json
from medicine import Medicine

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def get_user_file(username):
    return os.path.join(DATA_DIR, f"{username}.json")

def load_medicines(username):
    filepath = get_user_file(username)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
                return [Medicine(**med) for med in data]
            except:
                return []
    return []

def save_medicines(username, medicines):
    filepath = get_user_file(username)
    with open(filepath, 'w') as f:
        data = [med.__dict__ for med in medicines]
        json.dump(data, f)
