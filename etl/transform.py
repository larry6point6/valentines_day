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
