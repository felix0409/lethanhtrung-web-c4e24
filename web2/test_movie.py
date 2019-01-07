# 1. Connect to database

import mlab
from mongoengine import Document, StringField, IntField
mlab.connect()

# 2. Define model (document)
class Movie(Document):
    title = StringField()
    image = StringField()
    link = StringField()
    rate = IntField()


movie_list = Movie.objects(rate__gte=5, title__icontains="MIssIon") #search all    #lazy loading
for m in movie_list:
    print(m.title, m.rate)

# # 3. Create data
# m = Movie(title="Wall-E", 
#         image="https://images-na.ssl-images-amazon.com/images/I/91YTk3e7c-L._RI_.jpg", 
#         link="https://www.imdb.com/title/tt0910970/?ref_=tt_rec_tt", 
#         rate=6)

# m.save()