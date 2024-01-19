#import flask
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#setup application (name references this file)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://username:password@localhost:5432/dbname'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	date_creates = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

#Define function for the index route so we don't 404 (give url string for route)
#define function for the route, index returns a string.
@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		task_content = request.form['content']
		new_task = Todo(content=task_content)
		
        try:
            db.session.add(new_task)
			db.session.commit()
			return redirect('/')
        except:
            return 'There was an issue adding your task'
	
	else:
		#you could also do .first to grab the first in the date but we aint doign that
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
	#debug=true so if there are errors we can see on the webpage
	app.run(debug=True)
