from players import Player
import random
class Champion(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment):
        return random.choice(['rock', 'paper', 'scissors'])