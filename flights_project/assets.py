from dagster import asset
from dagster_duckdb import DuckDBResource

from flights_project import api


@asset
def airlines(duckdb: DuckDBResource):
    df = api.get_airlines()
    print(f'got {len(df)} airlines')

    with duckdb.get_connection() as conn:
        conn.execute('CREATE OR REPLACE TABLE airlines AS SELECT * FROM df')


@asset
def destinations(duckdb: DuckDBResource):
    df = api.get_destinations()
    print(f'got {len(df)} destinations')

    with duckdb.get_connection() as conn:
        conn.execute('CREATE OR REPLACE TABLE destinations AS SELECT * FROM df')


@asset
def flights(duckdb: DuckDBResource):
    df = api.get_flights()
    print(f'got {len(df)} destinations')

    with duckdb.get_connection() as conn:
        conn.execute('CREATE OR REPLACE TABLE flights AS SELECT * FROM df')


@asset
def aircrafttypes(duckdb: DuckDBResource):
    df = api.get_aircrafttypes()
    print(f'got {len(df)} destinations')

    with duckdb.get_connection() as conn:
        conn.execute('CREATE OR REPLACE TABLE aircrafttypes AS SELECT * FROM df')
