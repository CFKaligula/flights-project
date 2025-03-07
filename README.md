# flights_project

This is a [Dagster](https://dagster.io/) project which contains data pipelines for the [Schiphol Flights API](https://www.schiphol.nl/en/developer-center/explore-all-schiphols-apis-in-the-developer-center/).

## Installation

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

4 types of data are extracted from the API:

* flights
* destinations
* airlines
* aircrafttypes

These are requested from the API and the responses are processed and stored in a local [DuckDB](https://duckdb.org/) database file.

From these raw data tables, a processed view is created using [dbt](https://www.getdbt.com/):

* `full_flights`, which contain flight data combined with data from the other 3 tables. For example, instead of the destination code, the entire name of the destination is included.

With the new table, 2 other tables are then created:

* `airline_stats`, which contains the number of flights per airline
* `aircraft_stats`, which contains the number of flights per aircraft

From these statistics tables we create 2 pie chart visualizations:

* [Airline/Flight Pie Chart](./airline_pie_chart.html)
* [Aircraft/Flight Pie Chart](./aircrafttype_pie_chart.html)
