from flask import Flask, render_template, redirect

study1 = Flask(__name__)

@study1.route("/")
def home():
    return "This is the homepage"

@study1.route("/about-me")
def about_me():
    me = {
        "Name": "Trung",
        "Job": "Student",
        "School": "Bach Khoa University",
        "Hobbies": ["Playing videogames", "Listening to musik"]
    }
    return render_template("aboutme.html", me = me)

@study1.route("/school")
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == "__main__": 
    study1.run(debug=True)