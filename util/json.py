import json

def load_file(path):
    with open(path, "r") as f:
        return json.load(f)
