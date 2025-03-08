import pandas as pd
import requests

app_id = '72923fa7'
app_key = '253e9832649ed737526bfd030ef45c44'
MAX_PAGE_NUM = 20


def request_with_pagination(key):
    """
    https://developer.schiphol.nl/apis/flight-api/v4/flights?version=latest#/

    """
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


def request(key):
    headers = {'app_id': app_id, 'app_key': app_key, 'ResourceVersion': 'v4'}
    response = requests.get(
        f'https://api.schiphol.nl/public-flights/{key}',
        headers=headers,
    )
    return response.json()


def get_df_from_api(key: str):
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
