from flask import Flask, render_template, url_for, request
import mlab
from mongoengine import Document, StringField, IntField
mlab.connect()

class Users(Document):
  name = StringField()
  email = StringField()
  username = StringField()
  password = StringField()

app = Flask(__name__)
@app.route("/")
def home():
  return ''

@app.route("/register", methods=['POST', 'GET'])
def register():
  if request.method == "GET":
    return render_template('serious1.html')
  if request.method == "POST":
    u = Users(name=request.form['name'], 
              email=request.form['email'], 
              username=request.form['username'], 
              password=request.form['password'])
    u.save()
    return "You signed up successfully!"

if __name__ == '__main__':
  app.run(debug=True)