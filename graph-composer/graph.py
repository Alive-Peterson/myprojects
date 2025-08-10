import random

class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent = {}
        self.neighbours = []
        self.neighbours_weights = []

    def add_edge_to(self, vertex, weight=0):
        #adding an edge to the vertex we input as weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        #incrementing the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        pass

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbours_weights.append(weight)

    def next_word(self):
        #randomly selects the next word based on weights
        return random.choices(self.neighbours, weights=self.neighbours_weights)


# making a graph class

class Graph(object):
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, value):
        #returns all the possible words
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        #what if the value isn't in the graph?
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]  #gets the vertex 
    
    def get_next_word(self, current_vertex):
        self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probabilty_map()
