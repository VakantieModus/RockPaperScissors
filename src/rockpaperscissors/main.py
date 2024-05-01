"""Main module."""
from players import RandomPlayer, StonePlayer, ScissorPlayer, Win_Stay_Lose_Switch, Win_Switch_Lose_Change, PaperPlayer
from champion import Champion
from environment import RockPaperScissorsEnvironment

def simulate_game(player1, player2, num_games ,game_type, verbose):
    env = RockPaperScissorsEnvironment(player1, player2, game_type=game_type)
    for i in range(num_games):
        env.reset()
        done = False

        while not done:
            action1 = player1.choose_action(env)
            action2 = player2.choose_action(env)

            _, reward = env.step((action1, action2))

            if reward == 1:
                env.game_state[player1.name] += 1
            elif reward == -1:
                env.game_state[player2.name] += 1
            else:
                env.game_state['tie'] += 1

            done = env.game_done()
         


        result = env.get_winner()
        env.history[result] += 1
        if verbose:
            print(f'Game {i}: {result}')
            print(f'Scores: {[ (key, value) for key, value in env.game_state.items() ]}')
            print('----------------------------------------------')

    print(f'Final score over {num_games} games:')
    print(f'Scores: {[ (key, value) for key, value in env.history.items() ]}')


def main():
    player1 = Champion("KAMPIOENEN-player")
    player2 = StonePlayer("Stone-player")
    num_games = 20
    game_type = 1
    verbose = False
    simulate_game(player1, player2, num_games, game_type, verbose)

if __name__ == "__main__":
    main()
