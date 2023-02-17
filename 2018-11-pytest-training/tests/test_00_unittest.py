import json
import unittest

from the_code import second_element


class BasicSecondElementTest(unittest.TestCase):

    def test_get_second_element_from_list(self):
        my_list = ['red', 'green', 'blue']
        self.assertEqual('green', second_element(my_list))

    def test_get_second_element_from_empty_list(self):
        with self.assertRaises(IndexError):
            second_element([])

    def test_get_second_element_for_short_list(self):
        with self.assertRaises(IndexError):
            second_element([':('])


class SecondElementTestWithAlphabet(unittest.TestCase):

    def setUp(self):
        super().setUp()
        with open('tests/alphabet.json') as f:
            self.alphabet = json.load(f)

    def tearDown(self):
        self.alphabet = None  # Absolutely unnecessary
        super().tearDown()

    def test_get_second_element_in_alphabet(self):
        self.assertEqual('b', second_element(self.alphabet))
