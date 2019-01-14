from flask import Flask, render_template, request
from models.new_bike import New_bike
import mlab

mlab.connect()
app = Flask(__name__)

@app.route('/')
def home():
    return "This is homepage ^^"

@app.route('/new_bike', methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("serious1.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        new_bike = New_bike(model=model, 
                                fee=fee, 
                                image=image, 
                                year=year)
        new_bike.save()
        return "Gotchaaaa"

if __name__ == '__main__':
  app.run(debug=True)