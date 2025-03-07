from dagster import Definitions
from dagster_duckdb import DuckDBResource

from flights_project.api_assets.assets import all_assets
from flights_project.api_assets.output_assets import all_output_assets
from flights_project.dbt.definitions import dbt_models, dbt_resource

# all_api_assets = load_assets_from_modules([assets])


# defs = Definitions.merge(
#     # dbt
#     dg.Definitions(
#         assets=[dbt_models],
#         resources={'dbt': dbt_resource},
#     ),
#     # api
#     Definitions(
#         assets=all_assets,
#         resources={'duckdb': DuckDBResource(database='db.duckdb')},
#     ),
# )

defs = Definitions(
    assets=[dbt_models] + all_assets + all_output_assets,
    resources={'duckdb': DuckDBResource(database='db.duckdb'), 'dbt': dbt_resource},
)
