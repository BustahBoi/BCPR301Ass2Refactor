from unittest.mock import patch, Mock, call
from unittest import mock
from unittest import TestCase
from interpreter.prompt import Shell
from interpreter.filehandler import FileTypeXLSX
from interpreter.validator import Validator
from interpreter import validator
import os.path


# Wesley
class TestPrompt(TestCase):
    # Wesley
    def setUp(self):
        self.shell = Shell()
        validator.a = Validator()

    # Wesley
    def tearDown(self):
        self.shell = None

    def test_load_xlsx(self):
        expected = type(FileTypeXLSX)
        self.shell.do_load("../Saves/data.xlsx")
        actual = type(self.shell.filehandler.file_type)
        self.assertIsInstance(actual, expected)

    def test_load_path(self):
        with patch("builtins.print") as thing:
            self.shell.do_load("../Saves")
        a_call = [call("Path is not a file")]
        thing.assert_has_calls(a_call)

    def test_load_no_path(self):
        with patch("builtins.print") as thing:
            self.shell.do_load("")
        a_call = [call("No path was specified, please try again")]
        thing.assert_has_calls(a_call)

    def test_load_not_exist(self):
        with patch("builtins.print") as thing:
            self.shell.do_load("thing.html")
        a_call = [call("Path is not a file")]
        thing.assert_has_calls(a_call)

    def test_load_database_no_data(self):
        user_input = ['local', 'test']
        with patch("builtins.input", side_effect=user_input):
            with patch("builtins.print") as thing:
                self.shell.do_load("database")
        a_call = [call("No data found")]
        thing.assert_has_calls(a_call)

    def test_load_no_save(self):
        user_input = ['local', 'test']
        with patch("builtins.input", side_effect=user_input):
            with patch("builtins.print") as thing:
                self.shell.do_save("testNotWork")
        a_call = [call("Please load data before attempting to save")]
        thing.assert_has_calls(a_call)

    def test_load_database_local(self):
        user_input = ['localTest', 'local', 'localTest2']
        with patch("builtins.input", side_effect=user_input):
            with patch("builtins.print") as thing:
                self.shell.do_load("../Saves/data.xlsx")
                self.shell.do_save("local")
                self.shell.do_load("database")
        a_call = [call('.xlsx'),
                  call('Error at entry: 9'),
                  call('Error at entry: 10'),
                  call('Error at entry: 17'),
                  call('Error at entry: 18'),
                  call('Error at entry: 22'),
                  call('Error at entry: 24'),
                  call('Error at entry: 28'),
                  call('Error at entry: 49'),
                  call('Error at entry: 50'),
                  call('Error at entry: 56'),
                  call('Error at entry: 60'),
                  call('result'),
                  call("Data has been loaded")]
        thing.assert_has_calls(a_call)

    def test_load_database_remote(self):
        user_input = ['localhost', 'root', '', 'test', 'remote', 'localhost', 'root', '', 'test']
        with patch("builtins.input", side_effect=user_input):
            with patch("builtins.print") as thing:
                self.shell.do_load("../Saves/data.xlsx")
                self.shell.do_save("remote")
                self.shell.do_load("database")
        a_call = [call('.xlsx'),
                  call('Error at entry: 9'),
                  call('Error at entry: 10'),
                  call('Error at entry: 17'),
                  call('Error at entry: 18'),
                  call('Error at entry: 22'),
                  call('Error at entry: 24'),
                  call('Error at entry: 28'),
                  call('Error at entry: 49'),
                  call('Error at entry: 50'),
                  call('Error at entry: 56'),
                  call('Error at entry: 60'),
                  call('result'),
                  call("Data has been loaded")]
        thing.assert_has_calls(a_call)
        self.shell.db_handler.drop_remote_table()

    def test_save_data_to_db(self):
        user_input = ['localTest']
        with patch("builtins.input", side_effect=user_input):
            with patch("builtins.print") as thing:
                self.shell.do_load("../Saves/data.xlsx")
                self.shell.do_save("local")
        a_call = [call('.xlsx'),
                  call('Error at entry: 9'),
                  call('Error at entry: 10'),
                  call('Error at entry: 17'),
                  call('Error at entry: 18'),
                  call('Error at entry: 22'),
                  call('Error at entry: 24'),
                  call('Error at entry: 28'),
                  call('Error at entry: 49'),
                  call('Error at entry: 50'),
                  call('Error at entry: 56'),
                  call('Error at entry: 60'),
                  call('result')]
        thing.assert_has_calls(a_call)

    def test_save_data_fail(self):
        user_input = ['localTest']
        with patch("builtins.input", side_effect=user_input):
            with patch("builtins.print") as thing:
                self.shell.do_load("../Saves/data.xlsx")
                self.shell.do_save("local")
        a_call = [call('.xlsx'),
                  call('Error at entry: 9'),
                  call('Error at entry: 10'),
                  call('Error at entry: 17'),
                  call('Error at entry: 18'),
                  call('Error at entry: 22'),
                  call('Error at entry: 24'),
                  call('Error at entry: 28'),
                  call('Error at entry: 49'),
                  call('Error at entry: 50'),
                  call('Error at entry: 56'),
                  call('Error at entry: 60'),
                  call('result')]
        thing.assert_has_calls(a_call)

    def test_save_data_to_invalid(self):
        user_input = ['local', 'test']
        with patch("builtins.input", side_effect=user_input):
            with patch("builtins.print") as thing:
                self.shell.do_load("../Saves/data.xlsx")
                self.shell.do_save("localTest")
        a_call = [call('.xlsx'),
                  call('Error at entry: 9'),
                  call('Error at entry: 10'),
                  call('Error at entry: 17'),
                  call('Error at entry: 18'),
                  call('Error at entry: 22'),
                  call('Error at entry: 24'),
                  call('Error at entry: 28'),
                  call('Error at entry: 49'),
                  call('Error at entry: 50'),
                  call('Error at entry: 56'),
                  call('Error at entry: 60'),
                  call('result'),
                  call('invalid database type')]
        thing.assert_has_calls(a_call)

    def test_graph(self):
        self.shell.do_load("../Saves/data.xlsx")
        user_input = ['Gender', 'BMI Sales', 'id age bmi']
        with patch('builtins.input', side_effect=user_input):
            self.shell.do_graph("bar testDoGraph")
        self.assertTrue(os.path.isfile("testDoGraph.html"))

    def test_cd_sub(self):
        expected = "D:\\Onedrive\\Course\\2018\\Semester 1\\BCPR301 - Advanced Progra" \
                   "mming\\Assignment 2\\GitKraken\\BCPR301Ass2Refactor\\interpreter"
        self.shell.do_cd("..")
        actual = self.shell.directory
        self.assertEqual(expected, actual)

    def test_cd_sub_sub(self):
        expected = "D:\\Onedrive\\Course\\2018\\Semester 1\\BCPR301 - Advanced Programming\\Assign" \
                   "ment 2\\GitKraken\\BCPR301Ass2Refactor"
        self.shell.do_cd("..")
        self.shell.do_cd("..")
        actual = self.shell.directory
        self.assertEqual(expected, actual)

    def test_cd_not_specified(self):
        with patch("builtins.print") as thing:
            self.shell.do_cd("")
        a_call = [call('No path was specified, please try again')]
        thing.assert_has_calls(a_call)

    def test_cd_invalid_folder(self):
        with patch("builtins.print") as thing:
            self.shell.do_cd("changed")
        a_call = [call("Not a valid directory")]
        thing.assert_has_calls(a_call)

    def test_pwd(self):
        with patch("builtins.print") as thing:
            self.shell.do_pwd("")
        a_call = [call("D:\\Onedrive\\Course\\2018\\Semester 1\\BCPR301 - Advanced Progra"
                       "mming\\Assignment 2\\GitKraken\\BCPR301Ass2Refactor\\interpreter")]
        thing.assert_has_calls(a_call)

    def test_quit(self):
        with patch("builtins.print") as thing:
            self.shell.do_quit("")
        a_call = [call("Quitting ......")]
        thing.assert_has_calls(a_call)

    # def test_cd_not_valid(self):
    #     with patch("builtins.print") as thing:
    #         self.shell.do_cd()
    #     a_call = [call('Type of none is invalid')]
    #     thing.assert_has_calls(a_call)










