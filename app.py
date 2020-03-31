from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import pymongo
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/podcast")
def podcast():
    return render_template("podcast.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/contact")
def about():
    return render_template("contact.html")


@app.route("/music_tier_list")
def music():
    return render_template("music_tier_list.html")


@app.route("/visuals")
def globe():
    return render_template("visuals.html")

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)