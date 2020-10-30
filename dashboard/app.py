
from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def main():

    return render_template("home.html")


@app.route("/name", methods=["GET", "POST"])
def name():
	return render_template("name.html")

@app.route('/data', methods=["GET", "POST"])
def data():
	# Data Format
	# [TIME, Temperature, Humidity]
	randomnumber = random() * 100
	response = make_response(json.dumps(randomnumber))
	response.content_type = 'application/json'
	return response

if __name__ == "__main__":
    app.run(debug=True)