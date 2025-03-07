from setuptools import find_packages, setup

setup(
    name='flights_project',
    packages=find_packages(exclude=['flights_project_tests']),
    install_requires=[
        'dagster==1.10.4',
        'duckdb',
        'dagster-cloud',
        'dagster-dbt',
        'dagster-duckdb',
        'dagster-duckdb-pandas',
        'requests',
        'pandas',
        'dbt-duckdb',
        'plotly',
    ],
    extras_require={'dev': ['dagster-webserver', 'pytest', 'types-setuptools', 'types-requests', 'pandas-stubs']},
)
