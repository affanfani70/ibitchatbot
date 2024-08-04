import json
import logging


def load_data(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        logging.debug(f"Loaded intents: {data['intents']}")
        return data["intents"]
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return []
