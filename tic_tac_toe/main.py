from Game.game import Game
from service.player_service import PlayerService


def play_game():
    print("\n")
    print("Welcome to Tic Tac Toe!")
    player_service = PlayerService()
    players = player_service.add_players()
    game = Game()
    game.initiate_turns()
    end_game = False
    while not end_game:
        for player in players:
            game.play_turn(player)
            game.print_board()
            check_tie = game.check_tie()
            check_win = game.check_win()

            if check_tie:
                end_game = True
                break
            if check_win:
                game.turns = check_win
                print("\n")
                print(f'And the winner is: {player.name}')
                game.print_board()
                end_game = True
                break


def replay():
    re_play = 'y'
    while re_play.lower() == 'y':
        play_game()
        print("\n")
        re_play = input("Would you like to play again? press y if you do.")


if __name__ == '__main__':
    replay()
