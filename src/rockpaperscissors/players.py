import random
class Player:
    """
    Basic class template all players should adhere to inorder for the environment to work
    """
    def __init__(self, name):
        self.name = name
        

    def choose_action(self):
        raise NotImplementedError("Subclasses must implement choose_action method.")

class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment, reward):
        return random.choice(['rock', 'paper', 'scissors'])

class StonePlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment, reward):
        return 'rock'
    
class ScissorPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment, reward):
        return 'scissor'
    
class PaperPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_action(self, environment, reward):
        return 'paper'
    
    
class Win_Stay_Lose_Switch(Player):
    """
    First move is random, after that strategy starts kicking in:
        Previous match won -- Stay
        Previous match lost -- Switch to another move randomly
    """
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.switch = {'rock':['paper', 'scissors'],
                       'paper':['rock', 'scissors'],
                       'scissors':['paper', 'rock']}

    def choose_action(self, environment, reward):

        if reward == -1:
            return random.choice(self.switch[environment.historical_moves[self.name][-1]])
        elif reward == 1:
            return environment.historical_moves[self.name][-1]
        else:
            return random.choice(['rock', 'paper', 'scissors'])
    
class Win_Switch_Lose_Change(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        self.switch = {'rock':['paper', 'scissors'],
                'paper':['rock', 'scissors'],
                'scissors':['paper', 'rock']}

    def choose_action(self, environment, reward ):
        if reward == 1:
            return random.choice(self.switch[environment.historical_moves[self.name][-1]])
        elif reward == -1:
            return environment.historical_moves[self.name][-1]
        else:
            return random.choice(['rock', 'paper', 'scissors'])
        
class Zhang_distr(Player):
    """
    Propabilities according to:
        Initial move - https://www.cmu.edu/dietrich/sds/ddmlab/papers/ZhangMoisanGonzalez2020.pdf#page=5&zoom=100,398,736
        Transitions - https://pubmed.ncbi.nlm.nih.gov/26843423/

    Transitions (upgrading, downgrading or staying) are dependent on previous outcome
    """
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        self.distribution_first = {'rock':0.222,
                'paper':0.4,
                'scissors':0.378}

        self.transition_probabilities = {
            -1: {'Stay': 0.33, 'Upgrade': 0.33, 'Downgrade': 0.33},
            0 : {'Stay': 0.34, 'Upgrade': 0.32, 'Downgrade': 0.34},
            1 : {'Stay': 0.33, 'Upgrade': 0.33, 'Downgrade': 0.34}
        }
        self.transition_up =  {'rock': 'paper',
                'paper': 'scissors',
                'scissors':'rock'}
        
        self.transition_down =  {'paper': 'rock',
                'scissors': 'paper',
                'rock':'scissors'}
        
        
    def choose_action(self, environment, reward ):
        if not reward:
            chosen_action = random.choices(list(self.distribution_first.keys()), weights=list(self.distribution_first.values()), k=1)
            return chosen_action[0]
        else:
            strat = random.choices(list(self.transition_probabilities[reward].keys()), weights=list(self.transition_probabilities[reward].values()), k=1)
            if strat == 'Stay':
                return environment.historical_moves[self.name][-1]
            
            elif strat == 'Upgrade':
                return self.transition_up[environment.historical_moves[self.name][-1]]
            else:
                return self.transition_down[environment.historical_moves[self.name][-1]]



