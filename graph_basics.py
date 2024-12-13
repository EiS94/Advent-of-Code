class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x={self.x}, y={self.y}"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Node:

    def __init__(self, position, char):
        self.position = position
        self.char = char
        self.neighbours = []

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return f"{self.position}, char: {self.char}"

    def get_neighbour_positions(self):
        neighbour_positions = [Position(self.position.x - 1, self.position.y),
                               Position(self.position.x + 1, self.position.y),
                               Position(self.position.x, self.position.y - 1),
                               Position(self.position.x, self.position.y + 1)]
        return neighbour_positions


class Graph:

    def __init__(self, nodes, matrix):
        self.nodes = nodes
        self.matrix = matrix

    def print_matrix(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                position = Position(x, y)
                node = self.nodes[position]
                print(node.char, end="")
            print("")
        print()


def parse_input_to_graph(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()

    matrix = []
    for line in lines:
        matrix.append(list(line))

    nodes = {}
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            char = matrix[y][x]
            node = Node(Position(x, y), char)
            nodes[Position(x, y)] = node

    for position in nodes.keys():
        node = nodes[position]
        neighbour_positions = node.get_neighbour_positions()
        for neighbour_position in neighbour_positions:
            if neighbour_position in nodes:
                neighbour = nodes[neighbour_position]
                if neighbour.char == node.char:
                    node.neighbours.append(neighbour)

    return Graph(nodes, matrix)

def dfs(nodes, start_node, end_node, path=None):
    if path is None:
        path = []
    path = path + [start_node]
    if start_node == end_node:
        return path
    for neighbour in start_node.neighbours:
        if neighbour not in path:
            new_path = dfs(nodes, neighbour, end_node, path)
            if new_path:
                return new_path
    return None


def bfs(nodes, start_node, end_node):
    visited = [start_node]
    queue = [start_node]
    path = []

    while queue:
        m = queue.pop(0)
        path.append(m)

        if m == end_node:
            return path

        for neighbour in m.neighbours:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return None
