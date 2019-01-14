from mongoengine import Document, StringField, IntField

class New_bike(Document):
    model = StringField()
    fee = IntField()
    image = StringField()
    year = IntField()
