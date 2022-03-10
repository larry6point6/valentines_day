import json
import logging

import pandas as pd
from db.base import engine


def load_file(path):
    with open(path, "r") as f:
        data = json.load(f)

    return data


def get_team_names(data):
    teams = {}
    for id in data.keys():
        teams[id] = data[id]["title"]
    return teams


def get_columns(data):
    columns = []
    for id in data.keys():
        columns = [id for id in data[id]["history"][0].keys()]

    return columns


def get_all_teams(teams, columns, data):
    dataframes = {}
    for id, team in teams.items():
        teams_data = []
        for row in data[id]["history"]:
            teams_data.append(list(row.values()))

        df = pd.DataFrame(teams_data, columns=columns)
        dataframes[team] = df
        logging.info(f"Added data for {team}")
    return dataframes


def add_coefficients(dataframes):
    for team, df in dataframes.items():
        dataframes[team]["ppda_coef"] = dataframes[team]["ppda"].apply(
            lambda x: x["att"] / x["def"] if x["def"] != 0 else 0
        )
        dataframes[team]["oppda_coef"] = dataframes[team]["ppda_allowed"].apply(
            lambda x: x["att"] / x["def"] if x["def"] != 0 else 0
        )
    return dataframes


cols_to_sum = [
    "xG",
    "xGA",
    "npxG",
    "npxGA",
    "deep",
    "deep_allowed",
    "scored",
    "missed",
    "xpts",
    "wins",
    "draws",
    "loses",
    "pts",
    "npxGD",
]
cols_to_mean = ["ppda_coef", "oppda_coef"]


def create_final_df(dataframes):
    frames = []
    for team, df in dataframes.items():
        sum_data = pd.DataFrame(df[cols_to_sum].sum()).transpose()
        mean_data = pd.DataFrame(df[cols_to_mean].mean()).transpose()
        final_df = sum_data.join(mean_data)
        final_df["team"] = team
        final_df["matches"] = len(df)
        frames.append(final_df)

    full_stat = pd.concat(frames)
    full_stat.sort_values("pts", ascending=False, inplace=True)

    return full_stat


def add_columns(df):
    df["position"] = range(1, len(df) + 1)
    df["xG_diff"] = df["xG"] - df["scored"]
    df["xGA_diff"] = df["xGA"] - df["missed"]
    df["xpts_diff"] = df["xpts"] - df["pts"]
    return df


cols_to_int = [
    "wins",
    "draws",
    "loses",
    "scored",
    "missed",
    "pts",
    "deep",
    "deep_allowed",
]

col_order = [
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


def prep_final_clubs_df(df):
    df = df[col_order]
    df[cols_to_int] = df[cols_to_int].astype(int)
    df.rename(columns={"missed": "goals_conceded"}, inplace=True)
    df.rename(columns={"scored": "goals_scored"}, inplace=True)
    df.set_index("position", inplace=True)

    return df


def prep_players_df(path):
    players_data = load_file(path)
    players_df = pd.DataFrame(players_data)
    players_df.rename(columns={"shots": "shots_taken"}, inplace=True)
    return players_df


def write_df(df, tablename):
    df.to_sql(tablename, con=engine, if_exists="replace")
    logging.info(f"Writing {tablename} to database")
