from fastavro import parse_schema
import json
from pprint import pprint

clients_schema_address = 'clients-v2.json'

with open(f"./schemas/clients/{clients_schema_address}") as f:
    schema = json.load(f)

parsed_schema = parse_schema(schema)

pprint(parsed_schema)