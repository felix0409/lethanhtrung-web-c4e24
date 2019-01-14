from flask import Flask, render_template, request, session, redirect
import mlab
from models.character import Character
from models.user import User

mlab.connect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "cDF2GWr8njaHhewr"


@app.route('/characters', methods=["GET", "POST"])
def characters():
    if "token" in session:
        characters_list = Character.objects() #find all
        return render_template("characters.html", characters_list = characters_list)
    else:
        return redirect("/login?next=/characters") #?next=/characters
  
@app.route('/character_form', methods=["GET", "POST"])
def character_form():
    if request.method == "GET":
        return render_template("character_form.html")
    if request.method == "POST":
        form = request.form
        name = form["name"]
        image = form["image"]
        rate = form["rate"]
        new_character = Character(name=name, image=image, rate=rate)
        new_character.save()
        return "gotcha"

@app.route('/character/<given_id>')
def character_detail(given_id):
    #1. get one character, based on given id
    # character = Character.objects(id=given_id).first() #rate__gte=3
    character = Character.objects().with_id(given_id) #danh cho ai co id
    if character is None:
        return "Not found"
    else: #2. render
        return render_template("character_detail.html", character=character)

@app.route("/")
def home():
    return ""

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_form.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]

        found_user = User.objects(username=username).first()
        if found_user is None:
            return "User not found"
        elif found_user.password != password:
            return "Invalid password"
        else:
            session["token"] = username
            next = request.args.get("next")
            if next is None or next == "":
                return "Logged in successfully"
            else:
                return redirect(next)

@app.route("/posts")
def posts():
    if "token" not in session:
        return redirect("/login?next=/posts")
    else:
        username = session["token"]

@app.route("/logout")
def logout():
    del session["token"]
    return redirect("/login")


if __name__ == '__main__':
  app.run(debug=True)