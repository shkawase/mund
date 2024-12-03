from pathlib import Path
import json
from validator import make_validator
import sys

def validate_single(filepath: str):
    validator = make_validator()
    with open(filepath) as json_data_file:
        json_data = json.load(json_data_file)
        try:
            validator.validate(json_data)
        except Exception as e:
            print('Validation failed:', filepath)
            print('Reason:', e)

if __name__ == "__main__":
    validate_single(sys.argv[1])
