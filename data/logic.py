from random import choice, randrange, randint
from os import listdir

users = []
items = []
active_user = ''

class Item:
    global items 
    def __init__(self,display_name,title,description):
        self.created_by = display_name
        self.title = title
        self.description = description
        self.avg_rating = float()
        self.image_src = ''
        self.reviews = []
        items.append(self)

    def reviewItem(username,rating):
        #obj should have an attribute that is a list of reviews. reviews are username, rating, and comment
        class Review:
            def updateAvgRating(self,rating):
                ratings_list = []
                for x in self.reviews[rating]:
                    ratings_list.append(x)
                avg = sum(ratings_list) / len(ratings_list)
                avg_rating = avg

            def updateReviews(self,x):
                self.reviews.append(x)
            def __init__(self,username,rating):
                self.reviewdict = {
                    'reviewer' : username,
                    'rating' : rating,
                }
                self.updateReviews(self.reviewdict)
                

# we want to figure out how reviews are stored (a list of objects?), and when is avg_rating refreshed?

class User:
    global users

    def __init__(self,username):
        self.display_name = username
        users.append(self)
        print('created user:'+self.display_name)

    def createItem(self,title):
        createdItem = Item(self.display_name,title)
        items.append(createdItem)

    def setActiveUser(username):
        global active_user
        active_user = username
        print('User {} has been made the active user'.format(username))


def demoUserActions(username): #function to create items for demo of site
    demoUser = User(username) #create the user
    demoUser.setActiveUser #make our user the active user
    image_path = './/static//jpg//'
    placeholder_imgs = listdir(image_path)

    for i in range(0,randint(2,8)):
        item = Item(username,'Dummy item {}'.format(i+1),'Item created by demoUserActions() function')
        item.avg_rating = randrange(1,5)
        item.image_src = image_path + choice(placeholder_imgs)
    


demoUserActions('test')
print('Created {} items total'.format(len(items)))
for x in items:
    print('Created {} with rating of {} and image {}'.format(x.title,x.avg_rating,x.image_src))