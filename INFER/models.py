from bson import objectid
from mongokit import Connection, Document
from uuid import UUID

class Event(Document):
    structure = {
        }

class User(Document):
    structure = {
        'email': basestring,
        'name': basestring,
    }

class Comment(Document):
    structure = {
        'event_id': objectid.ObjectId,
        'user_id': objectid.ObjectId,
        'text': basestring
    }

connection = Connection()

connection.register([Event, Comment, User])