from flask import Flask, render_template

serious12 = Flask(__name__)

@serious12.route("/")
def home():
    return "HOME"

@serious12.route("/user/<username>")
def user(username):
    user = {
        "trung": {
            "name": "Trung",
            "age": 19,
            "birthplace": "Hanoi"
        },
        "nguyenvana": {
            "name": "A",
            "age": 69,
            "birthplace": "Trai Dat"
        }
    }
    return render_template("user.html", user = user)
if __name__ == "__main__": 
    serious12.run(debug=True)
