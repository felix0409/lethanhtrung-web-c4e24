#Update, Delete
#Atomic => id
import mlab
from models.character import Character

mlab.connect()

#1. Update
#1.1 Read document
#1.2 Update document
character = Character.objects().with_id("5c34a5b04615af1d608f5ef1")
# character.update(set__rate=2, set__name="Aquawomen") #set__ #inc__ #
# # print(character.rate) #=> rate=7
# character.reload()
# print(character.rate) #=> rate=10


#2. Delete
#2.1 Read document
#2.2 Delete
character.delete()