import dagster as dg
import plotly.express as px
from dagster_dbt import get_asset_key_for_model
from dagster_duckdb import DuckDBResource

from flights_project.dbt.definitions import dbt_models


def make_n_flights_pie_chart(df, title):
    # merge all airlines with only one flight
    one_flight_total = len(df[df['n_flights'] == 1])
    df.loc[-1] = ['Others', one_flight_total]
    df = df[df['n_flights'] > 1]

    # Create a customer histogram and write it out to an HTML file
    names_column, values_column = list(df.columns)[:2]
    fig = px.pie(df, names=names_column, values=values_column, title=title)
    fig.update_layout(bargap=0.2)

    save_chart_path = f'{title.lower().replace(" ", "_")}_pie_chart.html'
    fig.write_html(save_chart_path, auto_open=False)


@dg.asset(
    deps=[get_asset_key_for_model([dbt_models], 'airline_stats')],
)
def airline_pie_chart(duckdb: DuckDBResource):
    # Read the contents of the customers table into a Pandas DataFrame

    with duckdb.get_connection() as conn:
        df = conn.sql('SELECT * FROM main.airline_stats').df()

    make_n_flights_pie_chart(df, 'Flights per Airline')


@dg.asset(
    deps=[get_asset_key_for_model([dbt_models], 'aircraft_stats')],
)
def aircrafttype_pie_chart(duckdb: DuckDBResource):
    # Read the contents of the customers table into a Pandas DataFrame

    with duckdb.get_connection() as conn:
        df = conn.sql('SELECT * FROM main.aircraft_stats').df()

    make_n_flights_pie_chart(df, 'Flights per Aircraft Type')


all_output_assets = [airline_pie_chart, aircrafttype_pie_chart]
all_output_assets = [airline_pie_chart, aircrafttype_pie_chart]
