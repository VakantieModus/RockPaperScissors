import random
class Player:
    """
    Basic class template all players should adhere to inorder for the environment to work
    """
    def __init__(self, name):
        self.name = name
        

    def choose_action(self, environment):
        raise NotImplementedError("Subclasses must implement choose_action method.")


class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment):
        return random.choice(['rock', 'paper', 'scissors'])

class StonePlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment):
        return 'rock'
    
class ScissorPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment):
        return 'scissor'
    
class PaperPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment):
        return 'paper'
    
    
class Win_Stay_Lose_Switch(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment):
        return 'paper'
    
class Win_Switch_Lose_Change(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment):
        return 'paper'