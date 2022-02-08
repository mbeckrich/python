class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Can add any attribute after the dot
# Attributes are what object will have
# Essentially variables of the object

# use self.id in class instead of this
# user_1.id = "001"
# user_1.username = "Marshall"

user_1 = User("001", "Marshall")
user_2 = User("002", "Lizzy")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
