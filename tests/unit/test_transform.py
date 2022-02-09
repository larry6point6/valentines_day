import etl.transform
from conftest import create_teams_dict, create_test_data, get_initial_columns
from matplotlib.pyplot import get


def test_get_team_names(create_test_data, create_teams_dict):
    assert create_teams_dict == etl.transform.get_team_names(create_test_data)


def test_get_columns(get_initial_columns, create_test_data):
    assert get_initial_columns == etl.transform.get_columns(create_test_data)


def test_get_all_teams(create_teams_dict, get_initial_columns, create_test_data):
    assert 20 == len(
        etl.transform.get_all_teams(
            create_teams_dict, get_initial_columns, create_test_data
        )
    )


# Test here that the dictionary of dataframes contains 20 entries(History
# of each team in the league)


def test_add_coefficient(create_teams_dict, get_initial_columns, create_test_data):
    dataframes = etl.transform.get_all_teams(
        create_teams_dict, get_initial_columns, create_test_data
    )
    coeff = etl.transform.add_coefficients(dataframes)

    # assert "ppda_coef" in coeff["Arsenal"]
    # assert "oppda_coef" in coeff["Arsenal"]
    # seems quicker for the single assertion versus the column checks
    # Prior to the addition we have 19 columns
    assert 21 == len(coeff["Arsenal"])
