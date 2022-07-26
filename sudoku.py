"""
Sudoko Solver
Robin Schmid
"""

class Sudoku():
    board = None

    def set_game(self, input_board):
        self.board = input_board

    def check_finished(self):
        count = 0
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j] == 0:
                    count += 1
        if count == 0:
            return 1

    def print_board(self):
        if self.board == None:
            print("No board loaded")
        else:
            out = self.board

            for i in range(0,9):
                str_out = ""
                if i % 3 == 0 and i != 0:
                    str_out += "---------------------\n"
                for j in range(0,9):
                    if j % 3 == 0 and j != 0:
                        str_out += "| "
                    str_out += str(out[i][j]) + " "
                print(str_out)
            print("\n")

    def logic(self, i_, j_):
        pos_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        i_block = (i_ // 3) * 3
        j_block = (j_ // 3) * 3

        # Check which numbers are possible in a row
        for i in range(0, 9):
            for p in pos_num:
                if self.board[i][j_] == p:
                    pos_num.remove(p)

        # Check which numbers are possible in a column
        for j in range(0,9):
            for p in pos_num:
                if self.board[i_][j] == p:
                    pos_num.remove(p)

        # Check which numbers are possible in a block
        for i in range(i_block, i_block + 3):
            for j in range(j_block, j_block + 3):
                for p in pos_num:
                    if self.board[i][j] == p:
                        pos_num.remove(p)

        # If only one number is possible, this must be there
        if len(pos_num) == 1:
            print("New number at position [{},{}] is {}".format(i_+1,j_+1,pos_num[0]))
            self.board[i_][j_] = pos_num[0]
            self.print_board()

if __name__ == '__main__':

    sud = Sudoku()

    num_games = 200

    start = [[0, 0, 0, 6, 0, 2, 0, 0, 0],
             [4, 0, 0, 0, 5, 0, 0, 0, 1],
             [0, 8, 5, 0, 1, 0, 6, 2, 0],
             [0, 3, 8, 2, 0, 6, 7, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 9, 4, 0, 7, 3, 5, 0],
             [0, 2, 6, 0, 4, 0, 5, 3, 0],
             [9, 0, 0, 0, 2, 0, 0, 0, 7],
             [0, 0, 0, 8, 0, 9, 0, 0, 0]]

    end =   [[1, 9, 3, 6, 7, 2, 4, 8, 5],
             [4, 6, 2, 3, 5, 8, 9, 7, 1],
             [7, 8, 5, 9, 1, 4, 6, 2, 3],
             [5, 3, 8, 2, 9, 6, 7, 1, 4],
             [6, 7, 4, 1, 3, 5, 2, 9, 6],
             [2, 1, 9, 4, 8, 7, 3, 5, 8],
             [8, 2, 6, 7, 4, 1, 5, 3, 9],
             [9, 4, 1, 5, 2, 3, 8, 6, 7],
             [3, 5, 7, 8, 6, 9, 1, 4, 2]]

    sud.set_game(start)

    for n in range(0, num_games):
        for i in range(0,9):
            for j in range(0,9):
                if sud.board[i][j] == 0:
                    sud.logic(i, j)

        if sud.check_finished():
            print("Game finished!")
            print("Number of games: {}".format(n))
            exit()
