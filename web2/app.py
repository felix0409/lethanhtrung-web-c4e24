from flask import Flask, render_template
app = Flask(__name__)

@app.route("/characters")
def characters():
    c_list = [
        {
            "name": "Thanos",
            "image": "https://vignette.wikia.nocookie.net/marvel-contestofchampions/images/7/74/Thanos_portrait.png/revision/latest?cb=20150830174115",
            "link": "http://marvelcinematicuniverse.wikia.com/wiki/Thanos"
        },
        {
            "name": "Spider man",
            "image": "https://vignette.wikia.nocookie.net/marvel-contestofchampions/images/0/0b/Spider-Man_%28Classic%29_portrait.png/revision/latest?cb=20150830075418",
            "link": "http://marvel-contestofchampions.wikia.com/wiki/Spider-Man_(Classic)"
        },
        {
            "name": "Captain America",
            "image": "https://vignette.wikia.nocookie.net/marvel-contestofchampions/images/1/11/Captain_America_%28WWII%29_featured.png/revision/latest?cb=20170214000413",
            "link": "http://marvel-contestofchampions.wikia.com/wiki/File:Captain_America_(WWII)_featured.png"
        }
    ]
    return render_template("character_list.html", 
                            character_list=c_list,)

@app.route("/names")
def names():
    name_list = ["Huy", "Duc", "Quan", "Trung", "Hien"]
    return render_template("name_list.html",
                            name_list=name_list)

@app.route("/food_items")
def foods():
    
    return render_template("food_items.html", food_items=food_items)

food_items = [
        {
            "name": "HAMBURGER",
            "image": "https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-12/256/hamburger.png",
            "link": "https://www.mcdonalds.com/us/en-us.html",
            "ytid": "EGimicvrCKk"
        },
        {
            "name": "MASHED POTATOES",
            "image": "https://i.pinimg.com/736x/9c/a7/d8/9ca7d83a61f223f990fb8a89ed1b80ed--mashed-turnip-recipes-healthy-mashed-potatoes.jpg",
            "link": "https://www.mcdonalds.com/us/en-us.html",
            "ytid": "x6O9SwocyKQ"
        },
        {
            "name": "CHICKEN NUDDGETS",
            "image": "https://a.wattpad.com/useravatar/chicken-nuggets.128.706899.jpg",
            "link": "https://www.mcdonalds.com/us/en-us.html",
            "ytid": "iqZ_fDuCi7g"
        }
    ]
@app.route("/food_detail/<int:index>")
def food_detail(index):
    food_item = food_items[index]
    return render_template("food_detail.html", food_items=food_item)


if __name__ == '__main__':
  app.run(debug=True)