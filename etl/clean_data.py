# Structure of the site is pretty simple this can be used for both clubs and players
import logging


def find_data(search_string, scripts):
    for el in scripts:
        string_with_json_obj = ""
        if search_string in str(el):
            string_with_json_obj = str(el).strip()

            return string_with_json_obj


def strip_json(json_string):
    ind_start = json_string.index("('") + 2
    ind_end = json_string.index("')")
    json_data = json_string[ind_start:ind_end]
    json_data = json_data.encode("utf8").decode("unicode_escape")
    return json_data


def write_json(data, filename):
    filepath = f"./data/{filename}.json"
    with open(filepath, "w") as f:
        logging.info(f"writing data to {filepath}")
        f.write(
            data,
        )
