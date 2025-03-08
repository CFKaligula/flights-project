# flights_project

This is a [Dagster](https://dagster.io/) project which contains data pipelines for the [Schiphol Flights API](https://www.schiphol.nl/en/developer-center/explore-all-schiphols-apis-in-the-developer-center/).

## Installation

Make sure you have Python 3.11 installed.

First, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open <http://localhost:3000> with your browser to see the project.

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `flights_project_tests` directory and you can run tests using `pytest`:

```bash
pytest flights_project_tests
```

## Functionality

### API

4 types of data are extracted from the API:

* flights
* destinations
* airlines
* aircrafttypes

These are requested from the API stored in a local [DuckDB](https://duckdb.org/) database file. No processing is done as we want to preserve the raw data as raw as possible.

### Processing

Using [dbt](https://www.getdbt.com/) we will now process the data in 3 steps.

First during the staging process we process the raw data. We get 4 new tables: `stg_flights`, `stg_airlines`, ...

Then in an intermediary table the info from the staging tables is combined together. `int_full_flights` is a view which contain flight data combined with data from the other 3 tables. For example, instead of the destination code, the full name of the destination is included.

Finally we have the tables that will actually be used, They make use of the intermediary table to extract useful information. 2 other tables are created:

* `airline_stats`, which contains the number of flights per airline
* `aircraft_stats`, which contains the number of flights per aircraft

### Visualization

From these statistics tables we create 2 pie chart visualizations:

* [Airline/Flight Pie Chart](./airline_pie_chart.html)
* [Aircraft/Flight Pie Chart](./aircrafttype_pie_chart.html)
