import random

from model.player import Player


class PlayerService:

    def add_players(self):
        players = []
        comp_player = {}
        is_against_comp = self.ask_against_comp()
        while is_against_comp is None:
            is_against_comp = self.ask_against_comp()
        if is_against_comp:
            comp_player = Player("Computer", "", False)
            human_players = 1
        else:
            human_players = 2

        for i in range(human_players):
            players.append(self.add_player(i + 1))
        if is_against_comp:
            players.append(comp_player)
        symbol = ""
        while not symbol:
            symbol = input("Please enter player's 1 symbol X/O or press any key for a random symbol: ").upper()
            print("You must enter a key")
        symbols = ['X', 'O']

        if symbol not in symbols:
            rand = random.randint(0, 1)
            symbol = symbols[rand]

        if symbol == 'X':
            other_symbol = 'O'
        else:
            other_symbol = 'X'
        players[0].symbol = symbol
        players[1].symbol = other_symbol
        return players

    def add_player(self, num_player):
        invalid_input = True
        is_human = True
        name = ""
        while invalid_input:
            name = input(f"Enter player's {num_player} name: ")
            error = self.check_player_name(name)
            if error:
                print(error)
            else:
                invalid_input = False

        return Player(name, "", is_human)

    @staticmethod
    def check_player_name(name):
        if not name.strip():
            return "Please enter a name"
        elif any(char.isdigit() for char in name):
            return "Your name cannot have digits in it"
        return None

    @staticmethod
    def ask_against_comp():
        is_against_comp = input("Do you want to play against the computer? Y/N: ")
        if is_against_comp.lower() == 'y':
            return True
        elif is_against_comp.lower() == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'")
            return None

