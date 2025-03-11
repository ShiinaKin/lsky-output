from dataclasses import dataclass, field
import os
import yaml


@dataclass
class Config:
    # dialect+driver://username:password@host:port/database
    db_url: str = "mysql+mysqlconnector://root:123456@localhost:3306/lsky"
    output_path: str = "./output"
    output_schema_path: str = "/schema"


def get_config() -> tuple[Config, bool]:
    config_path = "./config.yml"

    if os.path.exists(config_path):
        print(f"Config file found.")
        with open(config_path, "r", encoding="utf-8") as f:
            config_data = yaml.safe_load(f)
        print("Configuration loaded successfully.")
        return Config(**config_data), True
    else:
        print(f"Config file not found. Creating default config.")
        default_config = Config()
        config_data = {
            "db_url": default_config.db_url,
            "output_path": default_config.output_path,
            "output_schema_path": default_config.output_schema_path
        }

        with open(config_path, "w", encoding="utf-8") as f:
            yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
        print("Default configuration file created.")
        return Config(**config_data), False
