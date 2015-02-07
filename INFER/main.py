from models import Event, User, Comment
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.mongokit import MongoKit, BSONObjectIdConverter
import os

app = Flask(__name__)
app.debug = True
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_DATABASE'] = 'test'

db = MongoKit(app)
db.register([Event, User, Comment])

app.url_map.converters['objectid'] = BSONObjectIdConverter


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
def create():
    return render_template('create.html')

@app.route('/new_event', methods=['POST'])
def create_event():
    title = request.form['title']
    name = request.form['name']
    email = request.form['email']
    ev = db.Event()
    user = list(db.User.find({'email':email}))
    if not user:
        user = db.User()
        user.email = email
        user.name = name
        user.save()
    else:
        user = user[0]
    ev.creator = user
    ev.title = title
    ev.save()
    return redirect(url_for('get_event', event_id = ev._id))


@app.route('/<objectid:event_id>')
def get_event(event_id):
    ev = db.Event.get_or_404(event_id)
    comments = list(db.Comment.find({'event_id': event_id}))
    return 'Hello World'

if __name__ == "__main__":
    app.run()
