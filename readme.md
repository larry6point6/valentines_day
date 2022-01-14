# Readme

I am going to build a minimal project that will allow a user to search for football statistics.

Google generally does a fantastic job of providing stats about football, i.e  how many goals has Salah scored this season? Will return something like this

![Salah goals scored search results](mo_salah_search.png)

This is great as you instantly get the information you need but what if you wanted to deeper, i.e something like which player has the highest average rating in the premier league, you don't get the nice answer in browser, you get a link to a website like so.

![Highest xg query](highest_average_rating.png)

This idea/project is borne mostly of me wanting to explore some new technology I haven't

## Plan

The scope is going to be limited to the premier league and will contain information from this season. There may well be scope in the future to add additional leagues, and historic statistical information. The players will all be those currently with clubs.

The data model will also be initially that of a minimal scope consisting of three tables Clubs, Players and Stats. The relationships are demonstrated below in an ERD diagram.

![Football Stats ERD](football_stats_erd.png)

One club can have many players, one player can only have one stat entry.

The data that will fill this database is going to data that is scraped from sites with the relevant information using a combination of the requests and the beautiful soup modules in Python.

Once this is completed, some cleaning of the data is next then it can placed into our current sqlite database.

Then connecting up the GPT3 to build out the query side of things.
