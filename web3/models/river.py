from mongoengine import Document, StringField, IntField

class Africa(Document):
    name = StringField()
    image = StringField()
    rate = IntField()