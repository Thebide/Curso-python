import json

def read_json(path: str) -> list[dict]:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        write_json(path, [])
        return []

def write_json(path: str, content: list[dict]) -> None:
    with open(path, "w") as file:
        json.dump(content, file, indent=1)