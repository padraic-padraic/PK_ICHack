from INFER.models import connection, Event
from flask import Flask, render_template

app = Flask(__name__)
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017

@app.route('/')
def create():
	return render_template('create.html')
