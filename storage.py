import json

def save_records(info):
    with open("accounts.json", "w") as file:
        json.dump(info, file)


def load_records():
    try:
        with open("accounts.json", "r") as file:
            return json.load(file) or {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}