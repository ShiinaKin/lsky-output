# lsky-output

将[lsky-pro](https://github.com/lsky-org/lsky-pro)的数据库数据导出为JSON文件

## Requirements

- Python 3.11+

## Usage

1. Clone the repository: `git clone https://gitclone.com/github.com/ShiinaKin/lsky-output.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the main script: `python main.py`
4. Modify the configuration file as needed
5. Run the main script again to output: `python main.py`

## Configuration

The application uses a YAML configuration file (`config.yml`). If not found, a default configuration will be created on first run.

Configuration options:

- `db_url`: Database connection string in SQLAlchemy format
  dialect+driver://username:password@host:port/database
- `output_path`: Directory for output files
- `output_schema_path`: Subdirectory for schema files

Example configuration:

```yaml
db_url: mysql+mysqlconnector://root:123456@localhost:3306/lsky
output_path: ./output
output_schema_path: /schema
```

## Output

- Schema files are saved to `{output_path}/{output_schema_path}/{schema_name}.json`
- A consolidated schema file is saved to `{output_path}/schema.json`

## License

[Apache License 2.0](LICENSE)