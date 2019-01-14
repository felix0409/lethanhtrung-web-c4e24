from mongoengine import Document, StringField

class User(Document):
    username = StringField()
    password = StringField() #khong bao h luu password nguoi dung vao he thong #hash string python

