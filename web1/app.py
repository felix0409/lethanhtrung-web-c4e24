from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")    #route #/: trang chu
def home():   #view function
    c = {
        "name": "AQUAMAN",
        "company": "DC Comics",
        "image": "https://www.aquamanmovie.com/assets/images/gallery/poster_aquaman.jpg",
        "ability": ["Speed", "Strength", "Reflexive", "Underwater", "Telepathy"]
    }
    
    return render_template("home.html", 
                            character=c)   # Response  #serve html

@app.route("/hi/<name>")
def say_hi(name):
    return "Hi " + name

@app.route("/add/<int:num1>/<int:num2>")
def sum(num1, num2):
    s = num1 + num2
    return str(s)


if __name__ == "__main__": 
    app.run(debug=True)   #den day la tao dc server roi #debug=True de k phai tat server
