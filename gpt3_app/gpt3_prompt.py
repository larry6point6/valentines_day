def generate_prompt(query):
    return """Return a SQL query

    Query: Which club has the most points.
    SQL: SELECT team FROM Clubs ORDER BY pts DESC LIMIT 1;
    Query: How many goals have Manchester City scored.
    SQL: SELECT goals_scored FROM Clubs where team = 'Manchester City';
    Query: Which team has the highest xg.
    SQL: SELECT team from Clubs ORDER BY xg DESC LIMIT 1;
    Query: Who has scored the most goals.
    SQL: SELECT player from Players ORDER BY goals DESC Limit 1;
    Query: Who are the three highest scorers.
    SQL: SELECT player from Players ORDER BY goals DESC Limit 3;
    Query: {}
    SQL:""".format(
        query
    )
