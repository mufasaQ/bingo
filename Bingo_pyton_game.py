
class robot:
    def __init__(self,Name):
        self.name= Name
        

    def say_hello(self):
        print("hello{}!".format(self.name))    

adam = robot('ada')

adam.say_hello()