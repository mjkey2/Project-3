#import flask
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#setup application (name references this file)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project3.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	date_creates = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
#Define function for the index route so we don't 404 (give url string for route)
#define function for the route, index returns a string.
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	#debug=true so if there are errors we can see on the webpage
	app.run(debug=True)
