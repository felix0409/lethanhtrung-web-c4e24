from flask import Flask, render_template, url_for, request
from pymongo import MongoClient

uri = "mongodb://<dbuser>:<dbpassword>@ds235022.mlab.com:35022/moviedb"
client = MongoClient(uri)
db = client.get_database()
user = db["users"]

app = Flask(__name__)

@app.route("/register", methods=['POST', 'GET'])
def register():
    return render_template('serious1.html')

@app.route("/registerdata", methods=['POST', 'GET'])
def registerdata():
  user_form = {
    "name": request.form['name'],
    "email": request.form['email'],
    "username": request.form["username"],
    "password": request.form["password"],
  }
  user.insert_one[user_form]
  client.close()
  return render_template("serious12.html", username=request.form['username'])
  # #  name=request.form['name'],
  #                           email=request.form['email'],
  #                           username=request.form['username'],
  #                           password=request.form['password']

if __name__ == '__main__':
  app.run(debug=True)