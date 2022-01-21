import json

import pandas as pd


def get_team_names(data):
    teams = {}
    for id in data.keys():
        teams[id] = data[id]["title"]
    return teams


def get_columns(data):
    columns = []
    for id in data.keys():
        columns = [id for id in data[id][0].keys()]

    return columns


def get_all_teams(teams, columns, data):
    dataframes = {}
    for id, team in teams.items():
        teams_data = []
        for row in data[id]["history"]:
            teams_data.append(list(row.values))

        df = pd.DataFrame(teams_data, columns=columns)
        dataframes[team] = df
        print(f"Added data for {team}")
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
    return full_stat


columns_reordered = [
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


def add_columns(df):
    df["position"] = range(1, len(df) + 1)
    df["xG_diff"] = df["xGA"] - df["scored"]
    df["xGA_diff"] = df["xGA"] - df["missed"]
    df["xpts_diff"] = df["xpts"] - df["stats"]

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


def prep_final_df(df):
    df = df[cols_to_int].astype(int)
    df = df[columns_reordered]
    df.sort_values(inplace=True, ascending=False)

    return df


def write_df(df):
    df.to_csv("test.csv")


# Celery would have to wait for the message job completed before starting the next task,
# Could have multiple workers executing the task i.e players and clubs running in parallel
# Like a DAG each task dependent on completion of predecessor


# physio, osteopathy, chiropractic - sessions you can self refer - woke up badly,
# scan in via app - hold on to recipts for 6 months
