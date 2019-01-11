from flask import Flask, render_template, request
from models.character import Character
import mlab
mlab.connect()

app = Flask(__name__)

@app.route('/character')
def home():
  return render_template("characters.html")

#character.objects()

@app.route('/add_character', methods=["POST", "GET"])
def add_character():
  # print(request.args.get('name'))

  # 1.Gui form
  if request.method == "GET":
    return render_template("character_form.html")
  elif request.method == "POST":
    # 2. Nhan form => luu
    form = request.form
    name = form['name']
    image = form['image']
    rate = form['rate']
    new_character = Character(name=name, image=image, rate=rate)
    new_character.save()
    return "Gotcha"


if __name__ == '__main__':
  app.run(debug=True)