#import dependencies
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from datetime import datetime as dt

#databse setup
engine = create_engine("postgres://SQL Tables-Updated/project3_database.db")
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save references to each table
CleanData_Table = Base.classes.CleanData_Table
LocationInfo = Base.classes.LocationInfo
EstablishmentMetrics = Base.classes.EstablishmentMetrics
EmploymentMetrics = Base.classes.EmploymentMetrics
WageMetrics = Base.classes.WageMetrics

session = Session(engine)
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Read the data from the CSV file
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    # Return the data as JSON
    return jsonify(data)


@app.route('/')
def dashboard()
	#list all available routes of data exploration
	 return """ <h1> Welcome to the Project 3 database api </h1>
    <h3> Available routes: </h3>
    <li><a href = "/api/v1.0/precipitation"> Precipitation</a>: <strong>/api/v1.0/precipitation</strong> </li>
    <li><a href = "/api/v1.0/stations"> Stations </a>: <strong>/api/v1.0/stations</strong></li>
    <li><a href = "/api/v1.0/tobs"> TOBS </a>: <strong>/api/v1.0/tobs</strong></li>
    <li>To retrieve the minimum, average, and maximum temperatures for a specific date, use <strong>/api/v1.0/&ltstart&gt</strong> (replace start with yyyy-mm-dd format)</li>
    <li>To retrieve minimum, average, and maximum temperatures for a start-end range, <strong>/api/v1.0/&ltstart&gt/&ltend&gt</strong> (replace both the start and end date in yyyy-mm-dd format)</li>
    </ul>
    """


@app.route('CleanData_Table')
def cleandata():

@app.route('LocationInfo')
def locationinfo():

@app.route('EstablishmentMetrics')
def establishmentmetrics():

@app.route('EmploymentMetrics')


@app.route('WageMetrics')
