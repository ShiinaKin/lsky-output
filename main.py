import json
import os

from decimal import Decimal
from datetime import date, datetime

import config
from util import get_engine, get_session, output_schema


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def serialize_schema(output_path: str, output_schema_path: str, schema_dict: dict):
    os.makedirs(f"{output_path}/{output_schema_path}", exist_ok=True)
    for schema_name, scheme_data in schema_dict.items():
        with open(f"{output_path}/{output_schema_path}/{schema_name}.json", "w") as file:
            file.write(json.dumps(scheme_data, cls=CustomJSONEncoder))
    with open(f"{output_path}/schema.json", "w") as file:
        file.write(json.dumps(schema_dict, cls=CustomJSONEncoder))

def output_image(strategy_schema: dict, output_path: str, output_image_path: str):
    print("Output image")
    local_strategy = list(filter(lambda strategy: strategy["key"] == 1, strategy_schema))
    print(f"Find local strategy: {[strategy['name'] for strategy in local_strategy]}")
    local_strategy = filter(lambda strategy: strategy["configs"]["root"] is not None, local_strategy)
    print(f"Find could be output local strategy: {[strategy['name'] for strategy in local_strategy]}")
    for strategy in local_strategy:
        source_folder = strategy['configs']['root']
        target_folder = f"{output_path}/{output_image_path}/{strategy['name']}"
        os.makedirs(target_folder, exist_ok=True)
        os.system(f"cp -r {source_folder} {target_folder}")
        print(f"Output images of strategy {strategy['name']} to {target_folder}")

def main():
    config_data, is_config_exist = config.get_config()
    if not is_config_exist:
        print("Please fill in the configuration file.")
        return
    engine = get_engine(config_data.db_url)
    db_session = get_session(engine)
    schema_dict = output_schema(db_session())
    serialize_schema(config_data.output_path, config_data.output_schema_path, schema_dict)
    if config_data.output_image:
        strategy_schema = schema_dict["strategy"]
        output_image(strategy_schema, config_data.output_path, config_data.output_image_path)
    print("Done.")


if __name__ == "__main__":
    main()
