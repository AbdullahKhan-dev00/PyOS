import json


def load_user():
    with open("data/users.json") as file:
        user_data = json.load(file)

def save_user(user):
  with open("data/users.json", "r") as file:
        loaded_data = json.load(file)
        with open("data/users.json", "w") as file:
            user_data = dict(user)
            loaded_data["users"].append(user)
            json.dump(loaded_data, file,)


def load_setting():
    with open("data/settings.json") as file:
        setting_data = json.load(file)

def save_settings(settings):
    with open("data/settings.json", "w") as file:
        json.dump("setting_to_save", file, indent=4)
