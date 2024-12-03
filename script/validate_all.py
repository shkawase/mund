from pathlib import Path
import json
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from jsonschema import validate, ValidationError, Draft202012Validator

SCHEMAS = Path("./schema/v0-alpha")

def load_schema():
    with open(SCHEMAS / 'data.schema.json') as schema_file:
        json_schema = json.load(schema_file)
    return json_schema

def retrieve_from_localfile(uri: str):
    path = SCHEMAS / Path(uri)
    contents = json.loads(path.read_text())
    return Resource.from_contents(contents)

def main():
    json_schema = load_schema()
    registry = Registry(retrieve=retrieve_from_localfile)
    validator = Draft202012Validator(json_schema, registry=registry)

    json_data_filelist = Path('json').glob('**/*.json')
    for json_data_file in json_data_filelist:
        json_data = json.loads(json_data_file.read_text())
        try:
            validator.validate(json_data, json_schema)
        except ValidationError as e:
            print('Validation failed:', json_data_file)
            print('Reason:', e)

if __name__ == "__main__":
    main()
