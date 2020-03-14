import numpy as np
from SlidingPuzzleUtils import Node, Queue
from SlidingPuzzleBoard import SlidingPuzzleBoard

class SlidingPuzzleSolver():

    def __init__(self, n_scrambles=25):
        self.puzzle = SlidingPuzzleBoard(board=np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]))
        self.puzzle.scramble(n_scrambles)

        self.init_node = Node(self.puzzle)
        self.queue = Queue()
        self.queue.add(self.init_node, self.heuristic(self.init_node.data))
        self.explored = []

        self.solution_path = None

    def solve_greedy(self):
        while self.queue.exists():
            node = self.queue.pop()
            if node.data.solved():
                self.solution_path = node.path()
                self.display()
                return True
            else:
                for direction in node.data.valid_moves():
                    child = node.child(node.data.copy_move(direction))
                    if child not in self.queue.nodes and child.data not in self.explored:
                        self.queue.add(child, self.heuristic(child.data))
                self.explored.append(node.data)
        return False

    def solve_astar(self):
        while self.queue.exists():
            node = self.queue.pop()
            if node.data.solved():
                self.solution_path = node.path()
                self.display()
                return True
            else:
                for direction in node.data.valid_moves():
                    child = node.child(node.data.copy_move(direction))
                    if child not in self.queue.nodes and child.data not in self.explored:
                        self.queue.add(child, self.heuristic(child.data) + len(child.path()) - 1)
                    elif child in self.queue.nodes:  # and not in explored?
                        child_value = self.heuristic(child.data) + len(child.path()) - 1
                        if child_value < self.queue.value(child):
                            self.queue.remove(child)
                            self.queue.add(child, child_value)
                self.explored.append(node.data)
        return False

    def heuristic(self, spb):
        current_indices = np.array([np.argwhere(spb.board == i)[0] for i in range(1, 16)])
        solution_indices = np.array([[i, j] for i in range(4) for j in range(4)])[:-1]
        return np.abs(current_indices - solution_indices).sum()

    def display(self):
        if self.solution_path:
            for node in self.solution_path:
                node.data.print()
            print('Solved')
            print('Path length:', len(self.solution_path)-1)
            print('Explored:', len(self.explored))
        else:
            print('No solution to display')

if __name__ == '__main__':
    puzzle = SlidingPuzzleSolver()
    puzzle.solve_astar()