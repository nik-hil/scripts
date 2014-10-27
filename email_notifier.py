'''Simple email notifier.
You can create multiple levels. for e.g
Level-1 -> level-2 -> level-3 or
Level-1 -> level-2a -> level-3a
        -> level-2b -> level-3b-> level4a

Attach post to desired level. Generally it is last level.
User notify method to send desired message.
'''
class Subscribe(object):
    def __init__(self, user=None):
        self.subscribe_set = set()
        if user:
            self.subscribe_set.add(user)
    def subscribe(self, user):
        # TODO: modify this to send email digest
        self.subscribe_set.add(user)
    def unsubscribe(self, user):
        self.subscribe_set.remove(user)



class Level(object):
    # TODO: create a base class Level. Implement class level1, level2, level3

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.child = set()
        self.subscribe_user = Subscribe()

    def __repr__(self):
        return self.level +" : "+ self.name
    
    def add(self,Level):
        # check if Level is of lower level-value
        self.child.add(Level)

    def remove(self, Level):
        # check if level is of lower level-value
        self.child.remove(Level)

    def get_child(self):
        return list(self.child)

    def subscribe(self, user):
        self.subscribe_user.subscribe(user)
        for child in get_child():
            child.subscribe(user)

    def unsubscribe(self, user):
        self.subscribe_user.unsubscribe(user)
        for child in get_child():
            child.unsubscribe(user)

    # TODO: create method email digest 
    def notify(self, *args, **kwargs):
        for child in self.get_child():
            child.notify( *args, **kwargs)
        
class Post(object):
    def __init__(self,Level,post,user):
        self.post = post
        self.author = user
        self.level = Level
        self.subscribe_user = Subscribe(user)
    
    def subscribe(self, user):
        self.subscribe_user.subscribe(user)

    def unsubscribe(self, user):
        self.subscribe_user.unsubscribe(user)
    
    # TODO: create method to send email digest
    def notify(self,*args, **kwargs):
        user_set = self.subscribe_user.subscribe_set
        for elem in user_set:
            print "Notified user: ", elem, " args: ", args, " kwargs:", kwargs


if __name__ == "__main__":
    sw_level1 = Level("Software","level1")
    release_level2 = Level("release Number", "level2")
    number_level3 = Level("1.2.3", "level3")
    sw_level1.add(release_level2)
    release_level2.add(number_level3)
    
    post1 = Post(number_level3, "Post1", "user1")
    post2 = Post(number_level3, "Post2", "user2")
    number_level3.add(post1)
    number_level3.add(post2)
    post1.notify("first dummy notice")

    post1.subscribe("user3")
    post1.notify("second dummy notice")
    sw_level1.notify("first sw_level notice")

    post1.unsubscribe("user1")
    sw_level1.notify("second sw_level notice")
