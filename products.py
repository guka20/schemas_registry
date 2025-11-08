from fastavro import parse_schema
from pprint import pprint
import json

products_schema_address = "products-v4.json"

with open(f"./schemas/products/{products_schema_address}") as f:
    schema = json.load(f)

parsed_schema = parse_schema(schema)
pprint(parsed_schema)