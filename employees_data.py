from fastavro import  parse_schema
import json
from pprint import pprint

employee_schema_address = "employee-v1.json"

with open(f"schemas/employee/{employee_schema_address}", 'r') as fo:
    schema = json.load(fo)

parsed_schema = parse_schema(schema)

pprint(parsed_schema)