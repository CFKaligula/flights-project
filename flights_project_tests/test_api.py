from fflights_project.api_assets.apiimport get_aircrafttypes, get_airlines, get_destinations, get_flights


def test_airlines():
    airline_df = get_airlines()
    first = airline_df.to_dict(orient='records')[0]
    print(first)
    assert len(airline_df) == 40
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
    assert len(df) == 40
    assert first == {'country': 'Sudan', 'iata': 'AAD', 'city': 'Ad-Dabbah', 'englishName': 'Ad-Dabbah', 'dutchName': 'Ad-Dabbah'}


def test_flights():
    df = get_flights()
    first = df.to_dict(orient='records')[3]
    print(first)
    assert len(df) == 40
    assert first == {'flightName': 'DL7488', 'gate': 'D82', 'prefixIATA': 'DL', 'aircraftTypeMain': '32S', 'aircraftTypeSub': '32Q', 'destination': 'TFS'}


def test_aircrafttypes():
    df = get_aircrafttypes()
    first = df.to_dict(orient='records')[0]
    print(first)
    assert len(df) == 40
    assert first == {'iataMain': '100', 'iataSub': '100', 'longDescription': 'FOKKER 100', 'shortDescription': 'FK100'}
