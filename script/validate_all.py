from pathlib import Path
import json
from validator import make_validator

def main():
    validator = make_validator()
    json_data_filelist = Path('json').glob('**/*.json')
    for json_data_file in json_data_filelist:
        json_data = json.loads(json_data_file.read_text())
        try:
            validator.validate(json_data)
        except Exception as e:
            print('Validation failed:', json_data_file)
            print('Reason:', e)

if __name__ == "__main__":
    main()
