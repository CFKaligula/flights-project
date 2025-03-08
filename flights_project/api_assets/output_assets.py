import dagster as dg
import pandas as pd
import plotly.express as px
from dagster_dbt import get_asset_key_for_model
from dagster_duckdb import DuckDBResource

from flights_project.dbt.definitions import dbt_models

"""
Contain assets to create visualisations from processed data
"""


def make_n_flights_pie_chart(df: pd.DataFrame, title: str) -> None:
    """
    Expects a dataframe with 2 columns,
    the first is a list of names and the second a list of the number of flights per name.
    Creates a pie chart and saves it
    """
    # e.g "airlines" and "n_flights"
    names_column, values_column = list(df.columns)[:2]

    # merge all names with only one flight
    one_flight_total = len(df[df[values_column] == 1])
    df.loc[-1] = ['Others', one_flight_total]
    df = df[df[values_column] > 1]

    fig = px.pie(df, names=names_column, values=values_column, title=title)
    fig.update_layout(bargap=0.2)

    save_chart_path = f'{title.lower().replace(" ", "_")}_pie_chart.html'
    fig.write_html(save_chart_path, auto_open=False)


@dg.asset(deps=[get_asset_key_for_model([dbt_models], 'airline_stats')])
def airline_pie_chart(duckdb: DuckDBResource):
    """
    Creates a pie chart with the # of flights per airline
    """

    with duckdb.get_connection() as conn:
        df = conn.sql('SELECT * FROM main.airline_stats').df()

    make_n_flights_pie_chart(df, 'Flights per Airline')


@dg.asset(deps=[get_asset_key_for_model([dbt_models], 'aircraft_stats')])
def aircrafttype_pie_chart(duckdb: DuckDBResource):
    """
    Creates a pie chart with the # of flights per aircraft type
    """

    with duckdb.get_connection() as conn:
        df = conn.sql('SELECT * FROM main.aircraft_stats').df()

    make_n_flights_pie_chart(df, 'Flights per Aircraft Type')


all_output_assets = [airline_pie_chart, aircrafttype_pie_chart]
