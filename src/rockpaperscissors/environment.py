class RockPaperScissorsEnvironment:
    def __init__(self,  player1, player2, game_type = 0,):
        """
        game_type(int): represents the type of rock paper scissors game that is played
            0: One-game only - players play games until one player wins
            1: Best out of three - players play three games, player with most points wins. Can end in a draw!
            2: First to three - players play untill one player reaches three points
        """
        self.valid_actions = ['rock', 'paper', 'scissors']

        self.player1 = player1.name
        self.player2 = player2.name

        self.game_state = {f'{self.player1}':0,
                           f'{self.player2}':0,
                           'tie':0}

        self.history = {f'{self.player1}':0,
                           f'{self.player2}':0,
                           'tie':0}
        
        self.historical_moves = {f'{self.player1}':[],
                           f'{self.player2}':[]}
        
        if game_type in [0,1,2]:
            self.game_type =  game_type
        else:
            raise ValueError(f"Error: unknown game_type = {game_type} supplied, choose from the following options:\n"
                            f"    0: One-game only - players play games until one player wins\n"
                            f"    1: Best out of three - players play three games, player with most points wins. Can end in a draw!\n"
                            f"    2: First to three - players play until one player reaches three points")


    def reset(self):
        # Reset the game to its initial state
        self.game_state = {f'{self.player1}':0,
                           f'{self.player2}':0,
                           'tie':0}
        
        self.historical_moves = {f'{self.player1}':[],
                           f'{self.player2}':[]}
    def get_winner(self):
        if self.game_state[self.player1] > self.game_state[self.player2]:
            return self.player1
        elif self.game_state[self.player1] == self.game_state[self.player2]:
            return 'tie'
        else:
            return self.player2
        
    def game_done(self,):
        if self.game_type == 0:
            return self.game_state[self.player1] > 0 or self.game_state[self.player2] > 0
        
        elif self.game_type == 1:
            return sum(self.game_state.values()) ==3
            
        elif self.game_type == 2:
            return self.game_state[self.player1] == 3 or self.game_state[self.player2] == 3


    def check_actions(self, action):
        if action not in self.valid_actions:
            return False
        else:
            return True
        
    def step(self, actions):
        # Take actions from two players and determine the outcome
        action1, action2 = actions

        reward = self._calculate_rewards(action1, action2)
        return reward

    def _calculate_rewards(self, action1, action2):
        # Calculate rewards based on the actions chosen by both players
        if action1 == action2:
            return 0  # Tie
        elif (action1 == 'rock' and action2 == 'scissors') or \
             (action1 == 'paper' and action2 == 'rock') or \
             (action1 == 'scissors' and action2 == 'paper'):
            return 1 # Player 1 wins, Player 2 loses
        else:
            return -1  # Player 1 loses, Player 2 wins
