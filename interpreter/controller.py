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

    def draw(self, x, y, title):
        self.graph.draw(x, y, title)


# Controller shouldn't run doctests???
# if __name__ == "__main__":
#     c = Controller()
#     doctest.testmod()

