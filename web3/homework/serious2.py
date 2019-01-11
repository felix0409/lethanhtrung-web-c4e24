from flask import Flask, render_template, request
from models.river import River
import mlab
mlab.connect()


app = Flask(__name__)

@app.route("/")
def home():
    return ""

@app.route('/africa')
def africa_list():
    list_ = River.objects(continent="Africa")
    return render_template("africa.html", list_ = list_)
@app.route('/samerica')
def river_samerica():
    list_ = River.objects(continent='S. America',length__lt=1000)
    return render_template('africa.html', list_=list_)

if __name__ == '__main__':
  app.run(debug=True)