from pathlib import Path
import json
from validator import make_validator
import sys


def validate_single_file(filepath: str):
    validator = make_validator()
    with open(filepath) as json_data_file:
        json_data = json.load(json_data_file)
        if isinstance(json_data, list):
            for i, json_entry in enumerate(json_data):
                try:
                    validator.validate(json_entry)
                except Exception as e:
                    print("Validation failed:", filepath)
                    print("entry#: ", i)
                    print("Reason:", e)
        else:
            try:
                validator.validate(json_data)
            except Exception as e:
                print("Validation failed:", filepath)
                print("Reason:", e)


if __name__ == "__main__":
    validate_single_file(sys.argv[1])
