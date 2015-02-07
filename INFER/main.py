from INFER.models import Event, User, Comment
from flask import Flask, render_template, request, redirect, url_for
from mongokit import Connection


app = Flask(__name__)
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017

con = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])
con.register([Event, User, Comment])
db = con.test.infer

@app.route('/')
def create():
    return render_template('create.html')

@app.route('/new_event', methods=['POST'])
def new_event():
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
    ev.creator = user
    ev.title = title
    ev.save()
    return redirect(url_for('get_event', event_id = ev._id))


@app.route('/<event_id>')
def get_event(event_id):
    ev = db.Event.find({'_id': event_id})
    comments = list(db.Comments.find({'event_id':ev._id}))
    return render_template('event.html', comments = comments, event = ev)

if __name__ == '__main__':
    app.run()
