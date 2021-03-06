# Readme

I am going to build a minimal project that will allow a user to search for football statistics.

Google generally does a fantastic job of providing stats about football, i.e  how many goals has Salah scored this season? Will return something like this

![Salah goals scored search results](mo_salah_search.png)

This is great as you instantly get the information you need but what if you wanted to deeper, i.e something like which team/club has the highest xg in the premier league, you don't get the nice answer in browser, you get a link to a website like so

![Highest xg query](highest_xg.png)

This idea/project is borne mostly of me wanting to explore some new technology I haven't used before which I think seems cool mostly gpt3

## Plan

The scope is going to be limited to the premier league and will contain information from this season. There may well be scope in the future to add additional leagues, and historic statistical information. The players will all be those currently with clubs. The initial iteration is going to use pipenv. If you want to explore the project, do the following:

1. Clone the repo, if you have a folder for projects clone it there ```git clone https://github.com/larry6point6/valentines_day``` this will create a directory called valentines_day
2. Start a virtual environment in the root directory using ```pipenv shell```
3. Then run ```pipenv install``` in the virtual environment, this will install all the required packages to run the project
4. You can access the database using SQL Alchemy or by using the following command ```sqlite ./db/football_stats.db``` from the root directory

### Data Model

The data model will be that of a minimal scope consisting of two tables Clubs and Players. The initial plan is displayed below consisting of three tables, Clubs, Players and Stats. The relationships are demonstrated below in an ERD diagram. This was before I explored the data.

![Football Stats ERD Initial](football_stats_erd.png)

With the thinking being that one club can have many players, one player can have more than one entry in the stat table by virtue of changing club etc, according to fifa rules, a player can only change teams three times within one season.

The original schema I envisioned is no longer fit for purpose, after exploring the data I realised the data was much richer data than I expected. In addition with the data available from understat, a seperate table for stats is not required. The new ERD is below.

![Football Stats updated ERD](football_stats_erd_updated.png)

One club can have many players, one player can have more than one entry(if they move clubs during the season etc)

The clubs table has been populated, the players table has also been populated. I am going to use alembic in order to manage the schema and database migrations. This will allow me to update/migrate the schema to a required structure and if there are any issues will also allow me the ability to roll the schemas back to earlier versions.

### Getting the Data

The data is provided via [understat](https://understat.com/), the data is JSON which needed some cleaning all of this is detailed in ```etl/transform.py```, with some reworking/modifications of the really nice work done [here](https://www.sergilehkyi.com/web-scraping-advanced-football-statistics/) initially did all the exploration in a jupyter notebook then abstracted the logic into mostly self contained functions, with a view to eventually/possibly using celery workers to call these functions. These functions could and will eventually probably be refactored.

Also added in some functionality to write the data to a JSON file to stop hammering the website with requests. If the data is present no request is made (detailed in ```main.py```), this could be further enhanced by suffixing a data identifier to the file path to ensure the most up to date data. In this current testing stage having the latest data isn't crucial.

All that's left to do is load the data, there is a function which does this in ```etl/transform.py```. This function loads the transformed tables into our database.

### GPT3

Then connecting up the GPT3 to build out the query side of things. The thinking here is that by leveraging gpt3's API we can generate SQL queries on the fly that will answer questions posed in a minimal flask app, all the code for this is stored in ```gpt3_app/``` directory. In order to run this and test the project yourself you can do the following(this assumes you already have your virtual environment activated)

1) Register for an API KEY with openai [here](https://openai.com/api/)
2) Fill in your api key in ```.env.example``` file, everything else is fine, just need to update the ```OPENAI_API_KEY``` variable with your key
3) Then in the root directory run this command ```mv .env.example .env```, if you are going to push this to github please remember to add the ```.env``` file to ```gitignore``` (more info [here](https://sebastiandedeyne.com/setting-up-a-global-gitignore-file/) or you can create a single ```gitignore``` file for this project) will protect your API KEY
4) Once that's done you just need to run the below:

   - ```cd gpt3_app/```
   - ```flask run``` (will run on port 5000, if port is in use can pass ```-p``` to specify an alternative port like ```5001```)

5) Enter your query and an answer will be returned from the database

GPT3 will generate some SQL and the project will run it and return your response from the database. If the question you ask, doesn't have an answer (or the table doesn't exist) you will get back a sqlalchemy error explaining the error like the below (I've cropped the image)

![SQL Error](sql_alechemy_error.png)

The error tells us what's wrong but we also see valid SQL code generated by GTP3, this error is because the table doesn't exist(at the time of writing). The question was "Who has scored the most goals?"

Now if you enter the question ```Which club has the highest xg```
![Highest xG question](highest_xg_question.png)

You get back the following response:
![Highest xG answer](highest_xg_answer.png)
