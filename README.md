# expense-saver

Compare same products from different shops.

## Setup migrations

```SHELL
alembic init alembic
alembic revision -m "initial"
alembic upgrade head
```

to replace the hardcoded db connection string in the .ini file.
Set: `sqlalchemy.url = $(DATABASE_URL)`.

In the `env.py` file, add:

- load env variables from `.env` file
- set `sqlalchemy.url` to env database url

```python
from dotenv import load_dotenv
load_dotenv()
config = context.config
section = config.config_ini_section
config.set_section_option(section, "sqlalchemy.url", os.environ["DATABASE_URL"])
```
