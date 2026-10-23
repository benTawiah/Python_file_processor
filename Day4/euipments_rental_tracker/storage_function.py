import json
import os

# Get the folder containing this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "rental.json")


def save_content(rental):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(rental, file, indent=4, ensure_ascii=False)


def load_content():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([], file)

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
