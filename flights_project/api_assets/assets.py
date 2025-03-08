from dagster import asset
from dagster_duckdb import DuckDBResource

from flights_project.api_assets import api


@asset(kinds={'duckdb'})
def airlines(duckdb: DuckDBResource):
    df = api.get_airlines()
    print(f'got {len(df)} airlines')

    with duckdb.get_connection() as conn:
        conn.execute('CREATE OR REPLACE TABLE raw_airlines AS SELECT * FROM df')


@asset(kinds={'duckdb'})
def destinations(duckdb: DuckDBResource):
    df = api.get_destinations()
    print(f'got {len(df)} destinations')

    with duckdb.get_connection() as conn:
        conn.execute('CREATE OR REPLACE TABLE raw_destinations AS SELECT * FROM df')


@asset(kinds={'duckdb'})
def flights(duckdb: DuckDBResource):
    df = api.get_flights()
    print(f'got {len(df)} destinations')

    with duckdb.get_connection() as conn:
        conn.execute('CREATE OR REPLACE TABLE raw_flights AS SELECT * FROM df')


@asset(kinds={'duckdb'})
def aircrafttypes(duckdb: DuckDBResource):
    df = api.get_aircrafttypes()
    print(f'got {len(df)} destinations')

    with duckdb.get_connection() as conn:
        conn.execute('CREATE OR REPLACE TABLE raw_aircrafttypes AS SELECT * FROM df')


all_assets = [airlines, destinations, flights, aircrafttypes]
