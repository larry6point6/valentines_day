import pathlib

import pretty_errors

from etl import clean_data, get_data, transform

string = "teamsData"
path = "./data/football_stats.json"


def run_get_data(path):
    path = pathlib.Path(path)
    if path.exists():
        print(f"Not downloading data again for {path} already downloaded today")
    else:
        data = get_data.download_data()

        soup = get_data.create_soup(data)

        json_string = clean_data.find_data(string, soup)

        json_string_cleaned = clean_data.strip_json(json_string)

        json_data = clean_data.write_json(json_string_cleaned)


def transform_data():

    data = transform.load_file(path)

    teams = transform.get_team_names(data)

    columns = transform.get_columns(data)

    all_teams_df = transform.get_all_teams(teams, columns, data)

    add_coeff = transform.add_coefficients(all_teams_df)

    final_df = transform.create_final_df(add_coeff)

    computed_cols = transform.add_columns(final_df)
    df = transform.prep_final_df(computed_cols)

    transform.write_df(df)


def main():

    run_get_data(path)
    transform_data()


if __name__ == "__main__":
    main()
