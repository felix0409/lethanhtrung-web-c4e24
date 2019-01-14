import mlab
from models.user import User
from models.post import Post

mlab.connect()

# a_random_user = User.objects(username="trung").first()
# if a_random_user is None:
#     print("User not found")
# else:
#     new_post = Post(title="Bai viet so 2 cua Trung", 
#                     content="Trung day haha",
#                     owner=a_random_user)
#     new_post.save()
#     print("Done saving...")

# #1. Post => Owner
# for post in Post.objects():
#     print(post.title, "by", post.owner.username) #. bet' nhe` (.)


#2. Owner => Post
user = User.objects(username="admin").first()
posts = Post.objects(owner=user)
print("Post owned by Admin: ")
for post in posts:
    print(post.title)