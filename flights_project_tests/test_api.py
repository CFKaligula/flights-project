﻿from flights_project.api_assets.api import get_aircrafttypes, get_airlines, get_destinations, get_flights


def test_airlines():
    airline_df = get_airlines()
    first = airline_df.to_dict(orient='records')[0]
    print(first)
    assert len(airline_df) == 370
    assert first == {
        'iata': '0B',
        'icao': 'BLA',
        'nvls': 5191,
        'publicName': 'Blue Air',
    }


def test_destinations():
    df = get_destinations()
    first = df.to_dict(orient='records')[3]
    print(first)
    assert len(df) == 400
    assert first == {
        'country': 'Sudan',
        'iata': 'AAD',
        'city': 'Ad-Dabbah',
        'publicName': {'dutch': 'Ad-Dabbah', 'english': 'Ad-Dabbah'},
    }


def test_flights():
    df = get_flights()
    first = df.to_dict(orient='records')[3]
    print(first)
    assert len(df) == 400
    # cannot contents check as they change per day


def test_aircrafttypes():
    df = get_aircrafttypes()
    first = df.to_dict(orient='records')[0]
    print(first)
    assert len(df) == 333
    assert first == {'iataMain': '100', 'iataSub': '100', 'longDescription': 'FOKKER 100', 'shortDescription': 'FK100'}
