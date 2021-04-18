class Player():

    def __init__(self, name):
        self.name = name
        self.choice = None
    
    def make_choice(self, choice):
        self.choice = choice
