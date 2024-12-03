from pathlib import Path
import json
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from jsonschema import Draft202012Validator

SCHEMAS = Path("./schema/v0-alpha")

def load_schema():
    with open(SCHEMAS / 'data.schema.json') as schema_file:
        json_schema = json.load(schema_file)
    return json_schema

def retrieve_from_localfile(uri: str):
    path = SCHEMAS / Path(uri)
    contents = json.loads(path.read_text())
    return Resource.from_contents(contents)

def make_validator():
    json_schema = load_schema()
    registry = Registry(retrieve=retrieve_from_localfile)
    validator = Draft202012Validator(json_schema, registry=registry)
    return validator