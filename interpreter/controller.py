from interpreter.database_handler import DatabaseHandler
from interpreter.filehandler import FileHandler
from interpreter.chart import Graph
from os import path

import doctest


# Wesley
class Controller:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.data = None
        self.filehandler = None
        self.graph = None

    def set_graph(self, graph_type, filename):
        self.graph = Graph()
        data = self.data
        self.graph.set_data(data, graph_type, filename)

    def set_criteria(self, criteria_1, criteria_2=None):
        self.graph.set_criteria(criteria_1, criteria_2)

    def set_keys(self, key_1, key_2=None):
        self.graph.set_keys(key_1, key_2)

    def draw(self, x, y, title):
        self.graph.draw(x, y, title)


# Controller shouldn't run doctests???
# if __name__ == "__main__":
#     c = Controller()
#     doctest.testmod()

