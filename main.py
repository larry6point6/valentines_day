# import pretty_errors

from etl import clean_data, get_data, transform

string = "teamsData"


def main():

    data = get_data.download_data()

    soup = get_data.create_soup(data)

    json_string = clean_data.find_data(string, soup)

    json_string_cleaned = clean_data.strip_json(json_string)

    json_data = clean_data.write_json(json_string_cleaned)


if __name__ == "__main__":
    main()
