from cgi import test

import pytest

from etl.transform import load_file


@pytest.fixture
def create_test_data():
    test_data = load_file("./tests/test_football_stats.json")
    return test_data


@pytest.fixture
def create_subset_test_data():
    subset_test_data = load_file("./tests/arsenal_subset.json")
    return subset_test_data


@pytest.fixture
def create_teams_dict():
    return {
        "71": "Aston Villa",
        "72": "Everton",
        "74": "Southampton",
        "75": "Leicester",
        "78": "Crystal Palace",
        "79": "Norwich",
        "80": "Chelsea",
        "81": "West Ham",
        "82": "Tottenham",
        "83": "Arsenal",
        "86": "Newcastle United",
        "87": "Liverpool",
        "88": "Manchester City",
        "89": "Manchester United",
        "90": "Watford",
        "92": "Burnley",
        "220": "Brighton",
        "229": "Wolverhampton Wanderers",
        "244": "Brentford",
        "245": "Leeds",
    }


@pytest.fixture
def get_initial_columns():
    return [
        "h_a",
        "xG",
        "xGA",
        "npxG",
        "npxGA",
        "ppda",
        "ppda_allowed",
        "deep",
        "deep_allowed",
        "scored",
        "missed",
        "xpts",
        "result",
        "date",
        "wins",
        "draws",
        "loses",
        "pts",
        "npxGD",
    ]


@pytest.fixture
def create_final_columns():
    return [
        "position",
        "team",
        "matches",
        "wins",
        "draws",
        "loses",
        "scored",
        "missed",
        "pts",
        "xG",
        "xG_diff",
        "npxG",
        "xGA",
        "xGA_diff",
        "npxGA",
        "npxGD",
        "ppda_coef",
        "oppda_coef",
        "deep",
        "deep_allowed",
        "xpts",
        "xpts_diff",
    ]
