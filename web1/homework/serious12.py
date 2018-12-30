from flask import Flask, render_template

serious12 = Flask(__name__)

@serious12.route("/")
def home():
    return "HOME"

@serious12.route("/bmi/<int:weight>/<int:height>")
def calc(weight, height):
    bmi = weight/((height/100)**2)
    return render_template("bmi.html", bmi = bmi)

if __name__ == "__main__": 
    serious12.run(debug=True)
