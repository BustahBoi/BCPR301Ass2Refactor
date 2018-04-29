from interpreter.validator import Validator
from interpreter import validator
from unittest import TestCase
import datetime


class TestValidator(TestCase):
    # James unit tests

    def setUp(self):
        self.validator = Validator()
        validator.a = Validator()
        self.maxDiff = None

    def tearDown(self):
        self.validator = None

    def test_valid_data(self):
        """
        Tests validating data
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                    5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'male', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'female', 'Age': '62', 'Sales': '245', 'BMI': 'normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_value_ID(self):
        """
        Tests validating data containing an invalid row value ID
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A2533', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_value_gen(self):
        """
        Tests validating data containing an invalid row value Gender
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'Toaster', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_value_age(self):
        """
        Tests validating data containing an invalid row value Age
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '692', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_value_sales(self):
        """
        Tests validating data containing an invalid row value Sales
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '2145', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_value_bmi(self):
        """
        Tests validating data containing an invalid row value BMI
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Gigantic', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_value_salary(self):
        """
        Tests validating data containing an invalid row value Salary
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '2350',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_value_birthday(self):
        """
        Tests validating data containing an invalid row value Birthday
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-19595'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_value_birthday_delimiter(self):
        """
        Tests validating data containing an invalid row value Birthday
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                    5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24:06:1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_key_ID(self):
        """
        Tests validating data containing an invalid key for ID
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'kjhID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_key_gen(self):
        """
        Tests validating data containing an invalid key for Gender
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Ge1nder': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_key_age(self):
        """
        Tests validating data containing an invalid key for Age
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Asge': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_key_sales(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sal5es': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_key_bmi(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BdMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_key_salary(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'S4alary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_invalid_key_birthday(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A233', 'Gender': 'F', 'Age': '62', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birsthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_id_type_error(self):
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23',
                                                       'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'male', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': dict(), 'Gender': 'female', 'Age': '62', 'Sales': '245', 'BMI': 'normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_gender_type_error(self):
        expected = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                        'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                       'BMI': 'Underweight', 'Salary': '23',
                                                       'Birthday': '05-05-1988'},
                    3: {'ID': 'A253', 'Gender': 'M', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                        'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                       'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'}}
        data = {1: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}, 2: {'ID': 'A244', 'Gender': 'M', 'Age': '30', 'Sales': '666',
                                                   'BMI': 'Underweight', 'Salary': '23', 'Birthday': '05-05-1988'},
                3: {'ID': 'A253', 'Gender': 'male', 'Age': '35', 'Sales': '456', 'BMI': 'Obesity', 'Salary': '23',
                    'Birthday': '01-08-1983'}, 4: {'ID': 'A262', 'Gender': 'M', 'Age': '24', 'Sales': '999',
                                                   'BMI': 'Normal', 'Salary': '23', 'Birthday': '24-05-1993'},
                5: {'ID': 'A253', 'Gender': dict(), 'Age': '62', 'Sales': '245', 'BMI': 'normal', 'Salary': '23',
                    'Birthday': '24-06-1995'}}
        result = Validator.save_dict(data)
        self.assertDictEqual(expected, result)

    def test_date_object(self):
        expected = "05-05-1988"
        data = datetime.datetime(1988, 5, 5)
        result = Validator.xlsx_date(data)
        self.assertEqual(expected, result)
