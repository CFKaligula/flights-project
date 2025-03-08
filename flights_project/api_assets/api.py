import os
from typing import Final

import dotenv
import pandas as pd
import requests

"""
This script contains functionality to communicate with the Schiphol Flights API.
The API can be found with the following link:
https://developer.schiphol.nl/apis/flight-api/v4/flights?version=latest#/
"""

APP_ID_KEY: Final = 'schiphol_api_app_id'
APP_KEY_KEY: Final = 'schiphol_api_app_key'

MAX_PAGE_NUM: Final = 20


def get_credentials() -> tuple[str, str]:
    """
    Load the variables in the local .env file into the environment variables
    """
    dotenv.load_dotenv()
    return os.environ[APP_ID_KEY], os.environ[APP_KEY_KEY]


def request_with_pagination(key: str) -> list[dict]:
    """
    Perform an API request to the Schiphol API using the given key and returns the json from the response.
    As to not overload the API we only load up to MAX_PAGE_NUM requests.
    Possible keys can be found in the documentation, for example 'flights'.
    """
    app_id, app_key = get_credentials()

    got_response = True
    responses = []
    page_num = 0
    while got_response and page_num < MAX_PAGE_NUM:
        response = requests.get(
            f'https://api.schiphol.nl/public-flights/{key.lower()}?page={page_num}',
            headers={'app_id': app_id, 'app_key': app_key, 'ResourceVersion': 'v4'},
        )

        if len(response.content) > 0 and response.content.decode() != 'Usage limit exceeded':
            responses.append(response.json())
            page_num += 1
        else:
            got_response = False

    return responses


def get_df_from_api(key: str) -> pd.DataFrame:
    """
    Collects the JSONs from the API requests and converts them into a Pandas DataFrame.
    """
    dicts = request_with_pagination(key)
    print(dicts)
    records = []
    for record_dict in dicts:
        records.extend(record_dict[key])

    df = pd.DataFrame.from_records(records)

    return df


def get_airlines() -> pd.DataFrame:
    return get_df_from_api('airlines')


def get_aircrafttypes():
    return get_df_from_api('aircraftTypes')


def get_destinations() -> pd.DataFrame:
    return get_df_from_api('destinations')


def get_flights():
    return get_df_from_api('flights')
