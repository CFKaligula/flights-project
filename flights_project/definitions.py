from dagster import Definitions
from dagster_duckdb import DuckDBResource

from flights_project.api_assets.assets import all_assets
from flights_project.api_assets.output_assets import all_output_assets
from flights_project.dbt.definitions import dbt_models, dbt_resource

defs = Definitions(
    assets=[dbt_models] + all_assets + all_output_assets,
    resources={'duckdb': DuckDBResource(database='db.duckdb'), 'dbt': dbt_resource},
)
