from fastavro import parse_schema
from pprint import pprint
import json

sales_schema_address = "sales-v2.json"

with open(f"./schemas/sales/{sales_schema_address}") as f:
    schema = json.load(f)

parsed_schema = parse_schema(schema)

pprint(parsed_schema)