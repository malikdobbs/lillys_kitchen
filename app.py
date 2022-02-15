import os
from flask import (
	Flask, flash, render_template, 
	redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
	import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


@app.route("/recipes")
def recipes():
	recipes = list(mongo.db.recipes.find())
	return render_template("recipes.html", recipes=recipes)


if __name__ == "__main__":
	app.run(host=os.environ.get("IP"),
			port=int(os.environ.get("PORT")),
			debug=True)
