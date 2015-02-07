from bson import objectid
from datetime import datetime
from mongokit import Document

class BaseDocument(Document):
    __database__ = 'test'
    __collection__ = 'infer'

class User(BaseDocument):
    structure = {
        'title': basestring,
        'email': basestring,
        'name': basestring,
    }
    user_dot_notation = True

class Event(BaseDocument):
    structure = {
        'creator': User,
        'created': datetime
    }
    default_values = {
        'created': datetime.now()
    }
    use_autorefs = True
    use_dot_notation = True

class Comment(BaseDocument):
    structure = {
        'event_id': objectid.ObjectId,
        'user': User,
        'text': basestring
    }
    use_dot_notation = True
    use_autorefs = True

