import json


def load_functions(file_path: str):
    with open(file_path, "r") as file:
        data = json.load(file)

        return data


functions = load_functions("data/input/functions_definition.json")
print(functions)
