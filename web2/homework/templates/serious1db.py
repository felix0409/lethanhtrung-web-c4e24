# 1. Connect to database

import mlab
from mongoengine import Document, StringField, IntField
mlab.connect()

# 2. Define model (document)
class Movie(Document):
    name = StringField()
    email = StringField()
    username = StringField()
    password = StringField()

# 3. Create data
m = Movie(name="{{name}}", 
        email="{{email}}", 
        username="{{username}}", 
        password="{{password}}")

m.save()