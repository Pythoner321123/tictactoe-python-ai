import sys
import random

class TicTacToe:
    def __init__(self):
        self.welcome_message = "Welcome to the Tic-Tac-Toe game!"
        self.board = [["1", "2", "3"],
                      ["4", "5", "6"],
                      ["7", "8", "9"]]
        self.player_mark = ''
        self.one_to_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.boxes_left = 9
        self.in_your_inventory = []
        self.in_pc_inventory = []

    def display_board(self):
        print(self.welcome_message)
        for row in self.board:
            print(row)

    def get_player_mark(self):
        self.player_mark = input("Choose your mark (Y/O): ").upper()
        if self.player_mark not in ['Y', 'O']:
            sys.exit("Invalid Input")

    def pc_move(self):
        try:
            pc_move = random.choice(self.one_to_nine)
            self.in_pc_inventory.append(pc_move)
            self.one_to_nine.remove(pc_move)
            row = (pc_move - 1) // 3
            col = (pc_move - 1) % 3

            if self.player_mark == 'Y':
                self.board[row][col] = 'X'
            else:
                self.board[row][col] = 'Y'
        except IndexError:
            if self.boxes_left == 0:
                print("Game Over")
                sys.exit()

    def check_win(self, inventory):
        win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for condition in win_conditions:
            if all(elem in inventory for elem in condition):
                return True
        return False

    def play(self):
        self.display_board()
        self.get_player_mark()
        while True:
            player_position = input(f'Choose with a number from 1-9 where you want to place your mark {self.player_mark}: ')
            try:
                player_position = int(player_position)
                if player_position not in range(1, 10):
                    raise ValueError("Input not in range 1-9")
                if player_position not in self.one_to_nine:
                    raise ValueError("Position already taken")
                self.in_your_inventory.append(player_position)
            except ValueError as e:
                print(f"Error: {e}")
                continue

            row = (player_position - 1) // 3
            col = (player_position - 1) % 3
            self.board[row][col] = self.player_mark
            self.one_to_nine.remove(player_position)
            self.boxes_left -= 1

            if self.check_win(self.in_your_inventory):
                print("You Won!")
                break

            self.pc_move()
            self.boxes_left -= 1

            if self.check_win(self.in_pc_inventory):
                print("PC Won!")
                break

            if self.boxes_left == 0:
                print("It's a tie!")
                break

            self.display_board()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
