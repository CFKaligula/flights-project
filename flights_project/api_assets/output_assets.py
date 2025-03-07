from pathlib import Path

import dagster as dg
import plotly.express as px
from dagster_dbt import get_asset_key_for_model
from dagster_duckdb import DuckDBResource

from flights_project.dbt.definitions import dbt_models


@dg.asset(
    deps=[get_asset_key_for_model([dbt_models], 'airline_stats')],
)
def airline_histogram(duckdb: DuckDBResource):
    # Read the contents of the customers table into a Pandas DataFrame

    with duckdb.get_connection() as conn:
        df = conn.sql('SELECT * FROM main.airline_stats').df()

    # Create a customer histogram and write it out to an HTML file
    fig = px.histogram(df, x='airlineName')
    fig.update_layout(bargap=0.2)
    fig.update_xaxes(categoryorder='total descending')
    save_chart_path = Path('../.').parent.joinpath('order_count_chart.html')
    fig.write_html(save_chart_path, auto_open=False)
