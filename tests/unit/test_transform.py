import etl.transform
from conftest import create_test_data


def test_get_team_names(create_test_data, create_teams_dict):
    assert create_teams_dict == etl.transform.get_team_names(create_test_data)


def test_get_columns(get_initial_columns, create_test_data):
    assert get_initial_columns == etl.transform.get_columns(create_test_data)
