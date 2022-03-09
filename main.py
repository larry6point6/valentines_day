import logging
import os
import pathlib

from dotenv import load_dotenv

from etl import clean_data, get_data, transform

load_dotenv()

team_string = os.getenv("TEAM_STRING")
player_string = os.getenv("PLAYER_STRING")
paths = [os.getenv("CLUB_STATS"), os.getenv("PLAYER_STATS")]


def run_get_data(paths):
    for path in paths:
        path = pathlib.Path(path)
        if path.exists():
            logging.info(
                f"Not downloading data again for {path} already downloaded today"
            )
    else:
        data = get_data.download_data()

        soup = get_data.create_soup(data)

        json_string_clubs = clean_data.find_data(team_string, soup)
        json_string_players = clean_data.find_data(player_string, soup)

        json_string_cleaned_clubs = clean_data.strip_json(json_string_clubs)
        json_string_cleaned_players = clean_data.strip_json(json_string_players)

        json_data_clubs = clean_data.write_json(json_string_cleaned_clubs, "club_stats")
        json_data_players = clean_data.write_json(
            json_string_cleaned_players, "player_stats"
        )


def transform_data():

    clubs_data = transform.load_file(paths[0])

    teams = transform.get_team_names(clubs_data)

    columns = transform.get_columns(clubs_data)

    all_teams_df = transform.get_all_teams(teams, columns, clubs_data)

    add_coeff = transform.add_coefficients(all_teams_df)

    final_df = transform.create_final_df(add_coeff)

    computed_cols = transform.add_columns(final_df)
    clubs_df = transform.prep_final_clubs_df(computed_cols)

    players_df = transform.prep_players_df(paths[1])

    transform.write_df(clubs_df, "clubs")
    transform.write_df(players_df, "players")


def main():
    logging.basicConfig(
        filename="football_stats.log",
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%d/%m/%y %H:%M:%S",
        filemode="w",
        level=logging.INFO,
    )
    logging.info("Started getting data")
    run_get_data(paths)
    logging.info("Starting data transformations")
    transform_data()
    logging.info("Transformations complete and database populated")


if __name__ == "__main__":
    main()
