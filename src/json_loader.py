from src.models import prompt, FunctionDefinition
import json


def load_function_definition(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [FunctionDefinition(**item) for item in data]

    except FileNotFoundError:
        raise RuntimeError(f"File not found: {path}")

    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON in {path}")


def load_prompt(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [prompt(**item) for item in data]

    except FileNotFoundError:
        raise RuntimeError(f"File not found: {path}")
