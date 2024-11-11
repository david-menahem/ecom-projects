import random


class Game:
    turns = []

    def initiate_turns(self):
        for i in range(0, 9):
            turn = " "
            self.turns.append(turn)

    def print_board(self):
        boxes = 9
        for i in range(boxes):
            if i % 3 == 0:
                print()
            print(f"[{self.turns[i]}]", end="")

    def play_turn(self, player):
        box = 0
        if player.is_human:
            error = " "
            while error:
                print(error)
                box = input("\n\nEnter a box location from 1 to 9: ")
                error = self.check_turn(box)
            box = int(box) - 1
            self.turns[box] = player.symbol
        else:
            print("\n\nThe computer's turn...")
            boxes_avail = self.boxes_left()
            box = random.choice(boxes_avail)
            self.turns[box] = player.symbol

        return box

    def check_turn(self, box):
        if box.isdigit():
            box = int(box) - 1
            if 0 <= box <= 8:
                if self.turns[box] == " ":
                    return False
                else:
                    error = "That box is taken!"
            else:
                error = "The number must be from 1 to 9"
        else:
            error = "The input must be a number"

        return error

    def check_tie(self):
        number_of_turns = 0
        for i in range(0, 9):
            if self.turns[i] != " ":
                number_of_turns += 1
            else:
                break

        if number_of_turns == 9:
            return True

    def boxes_left(self):
        boxes_avail = []
        for i in range(0, 8):
            if self.turns[i] == " ":
                boxes_avail.append(i)
        return boxes_avail

    def check_win(self):
        pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8, pos_9 = self.turns

        if pos_1 != " " and pos_1 == pos_2 and pos_2 == pos_3:
            return [pos_1, pos_2, pos_3, " ", " ", " ", " ", " ", " "]
        elif pos_4 != " " and pos_4 == pos_5 and pos_5 == pos_6:
            return [" ", " ", " ", pos_4, pos_5, pos_6," ", " ", " "]
        elif pos_7 != " " and pos_7 == pos_8 and pos_8 == pos_9:
            return [" ", " ", " ", " ", " ", " ", pos_7, pos_8, pos_9]
        elif pos_1 != " " and pos_1 == pos_4 and pos_4 == pos_7:
            return [pos_1, " ", " ", pos_4, " ", " ", pos_7, " ", " "]
        elif pos_2 != " " and pos_2 == pos_5 and pos_5 == pos_8:
            return [" ", pos_2, " ", " ", pos_5, " ", " ", pos_8, " "]
        elif pos_3 != " " and pos_3 == pos_6 and pos_6 == pos_9:
            return [" ", " ", pos_3, " ", " ", pos_6, " ", " ", pos_9]
        elif pos_1 != " " and pos_1 == pos_5 and pos_5 == pos_9:
            return [pos_1, " ", " ", " ", pos_5, " ", " ", " ", pos_9]
        elif pos_3 != " " and pos_3 == pos_5 and pos_5 == pos_7:
            return [" ", " ", pos_3, " ", pos_5, " ", pos_7, " ", " "]
        else:
            return False




