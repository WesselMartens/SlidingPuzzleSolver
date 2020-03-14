import numpy as np

class SlidingPuzzleBoard():

    def __init__(self, board=np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]])):
        self.board = board
        self.zero = np.argwhere(self.board == 0)[0]

    def __eq__(self, other):
        return (self.board == other.board).all()

    def valid_moves(self):
        moves = []
        if self.zero[0] > 0:
            moves.append(1) # up
        if self.zero[1] < 3:
            moves.append(2) # right
        if self.zero[0] < 3:
            moves.append(3) # down
        if self.zero[1] > 0:
            moves.append(4) # left

        return moves

    def calc_move(self, direction):
        row, col = self.zero
        valid_moves = self.valid_moves()
        if direction == 1 and direction in valid_moves:
            self.board[row][col] = self.board[row-1][col]
            self.board[row-1][col] = 0
            self.zero[0] -= 1

        elif direction == 2 and direction in valid_moves:
            self.board[row][col] = self.board[row][col+1]
            self.board[row][col+1] = 0
            self.zero[1] += 1

        elif direction == 3 and direction in valid_moves:
            self.board[row][col] = self.board[row+1][col]
            self.board[row+1][col] = 0
            self.zero[0] += 1

        elif direction == 4 and direction in valid_moves:
            self.board[row][col] = self.board[row][col-1]
            self.board[row][col-1] = 0
            self.zero[1] -= 1

    def copy_move(self, direction):
        new_spb = SlidingPuzzleBoard(np.copy(self.board))
        new_spb.calc_move(direction)
        return new_spb

    def scramble(self, steps):
        reverse = 0
        for _ in range(steps):
            direction = np.random.choice([move for move in self.valid_moves() if move != reverse])
            reverse = (direction + 5) % 4 + 1
            self.calc_move(direction)

    def reset(self):
        self.board = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]])
        self.zero = np.array([3,3])

    def solved(self):
        return (self.board == np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]])).all()

    def print(self):
        print(self.board)