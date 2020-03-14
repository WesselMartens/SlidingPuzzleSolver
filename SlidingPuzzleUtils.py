import numpy as np

class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent

    def child(self, data):
        return Node(data, self)

    def path(self):
        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        return list(reversed(path))

class Queue:

    def __init__(self):
        self.nodes = []
        self.values = []

    def pop(self):
        # note how queue pops node with minimal value
        idx = np.argmin(self.values)
        self.values.pop(idx)
        return self.nodes.pop(idx)

    def add(self, data, value):
        self.nodes.append(data)
        self.values.append(value)

    def remove(self, data):
        idx = self.nodes.index(data)
        del self.nodes[idx]
        del self.values[idx]

    def value(self, data):
        idx = self.nodes.index(data)
        return self.values[idx]

    def size(self):
        return len(self.nodes)

    def exists(self):
        return self.size() != 0