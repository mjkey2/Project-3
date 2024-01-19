#import flask
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#setup application (name references this file)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://username:password@localhost:5432/dbname'
db = SQLAlchemy(app)

#Define function for the index route so we don't 404 (give url string for route)
#define function for the route, index returns a string.
@app.route('/')
def dashboard()
	#list all available routes of data exploration

@app.route('query')


@app.route('info')

