from flask import Flask, render_template, request
import mlab
from models.character import Character

mlab.connect()
app = Flask(__name__)


@app.route('/characters', methods=["GET", "POST"])
def characters():
    characters_list = Character.objects() #find all
    return render_template("characters.html", characters_list = characters_list)
  
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


if __name__ == '__main__':
  app.run(debug=True)