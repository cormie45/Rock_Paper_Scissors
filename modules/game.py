import random
from modules.player import Player

def __init__(self, player_1, player_2=None):
    self.player_1 = player_1
    self.player_2 = player_2

    self.wins = [
        ["rock", "scissors"],
        ["rock", "lizard"],
        ["paper", "rock"],
        ["paper", "spock"],
        ["scissors", "paper"],
        ["scissors", "lizard"],
        ["lizard", "spock"],
        ["lizard", "paper"],
        ["spock", "rock"],
        ["spock", "scissors"]
    ]
    def get_winner(self, player):
        self.winning_player = player
    
    def result(self, player_1,player_2):
        if player_1.choice == player_2.choice:
            return None
        for game in self.wins:
            if [player_1.choice, player_2.choice] == game:
                self.get_winner(player_1)
                return self.winning_player
            elif [player_2.choice, player_1.choice] == game:
                self.get_winner(player_2)
                return self.winning_player

    def computer_rps(self):
        self.player_2 = Player("A.I.")
        self.player_2.choice = random.choice(["rock", "paper", "scissors"])

    def computer_rpsls(self):
        self.player_2 = Player("A.I.")
        self.player_2.choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])