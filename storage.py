import json

def save_records(info):
    with open("accounts.json", "w") as file:
        json.dump(info, file)


def load_records():
    with open("accounts.json", "r") as file:
        try:
            return json.load(file) or {}
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}