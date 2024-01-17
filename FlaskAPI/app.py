#import flask
from flask import Flask, render_template, url_for
#setup application (name references this file)
app = Flask(__name__)

#Define function for the index route so we don't 404 (give url string for route)
#define function for the route, index returns a string.
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	#debug=true so if there are errors we can see on the webpage
	app.run(debug=True)
