from dagster import Definitions, load_assets_from_modules
from dagster_duckdb import DuckDBResource

from flights_project import assets  # noqa: TID252

all_assets = load_assets_from_modules([assets])


defs = Definitions(
    assets=all_assets,
    resources={
        'duckdb': DuckDBResource(
            database='db.duckdb',  # required
        )
    },
)
