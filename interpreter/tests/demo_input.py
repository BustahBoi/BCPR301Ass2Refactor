from unittest.mock import patch
from unittest import TestCase


def answer():
    ans = input('enter yes or no')
    result = ""
    if ans == 'yes':
        result += 'yes'
    if ans == 'no':
        result += 'no'
    ans2 = input('enter 1 or 2')
    if ans2 == '1':
        result += '1'
    if ans2 == '2':
        result += '2'
    return result


class TestInput(TestCase):

    @patch('builtins.input', side_effect=['yes', '1'])
    def test_answer_yes(self, mock):
        self.assertEqual(answer(), 'yes1')

    def test_answer_yes2(self):
        user_input = ['no', '2']
        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(answer(), 'no2')

