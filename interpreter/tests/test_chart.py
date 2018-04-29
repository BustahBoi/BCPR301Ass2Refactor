from interpreter.chart import Graph, GraphType, BarGraph, Bar
from unittest import TestCase
import os.path


class TestGraph(TestCase):

    def setUp(self):
        self.graph = Graph()
        self.maxDiff = None

    def tearDown(self):
        self.graph = None

    def test_html_file_made(self):
        data = {1: {"ID": "A23", "Gender": "Male", "Age": 22, "Sales": 250, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"ID": "A2f3", "Gender": "Male", "Age": 23, "Sales": 250, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"ID": "Aa23", "Gender": "Female", "Age": 25, "Sales": 25, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                4: {"ID": "A23", "Gender": "Female", "Age": 26, "Sales": 250, "BMI": "normal", "salary": 20,
                "Birthday": "24/06/1995"}}
        self.graph.set_data(data, "pie", "pieTest.html")
        self.graph.set_criteria("Sales", 250)
        self.graph.set_keys("Gender", "Sales")
        self.graph.draw("Gender", "Sales", "Gender and Sales test")
        self.assertTrue(os.path.isfile("./pieTest.html"))

