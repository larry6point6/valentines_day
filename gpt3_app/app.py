import os

import openai
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from gpt3_prompt import generate_prompt

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():

    if request.method == "POST":
        query = request.form["query"]
        response = openai.Completion.create(
            engine="davinci",
            prompt=generate_prompt(query),
            temperature=0.4,
        )

        return redirect(url_for("index", result=response.choices[0].text.split(";")))

    result = request.args.get("result")
    print(result)

    if result is None:
        return render_template("index.html")

    else:
        answer = db.session.execute(result)

        result = answer.fetchone()

        return render_template("index.html", result=result[0])
