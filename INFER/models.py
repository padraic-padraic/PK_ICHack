from mongokit import Connection, Document
from uuid import UUID

class Event(Document):
    structure = {
        'id': UUID,
        }

class Comment(Document):
    structure = {
        'event_id': UUID,
        'user_id': basestring,
        'text': basestring
    }

connection = Connection()

connection.register([Event])