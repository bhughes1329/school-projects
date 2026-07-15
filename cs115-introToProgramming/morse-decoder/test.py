# === CS 115 Homework 2 Test===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Brooke Hughes
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 2 Test===

import hw2
import unittest

hw2.dictionary = ("AM", "AS", "BE", "BED", "CAN", "EGG", "HE", "HER", "HIM",
    "HIS", "ILL", "IS", "KID", "ME", "MY", "ON", "OR", "SEE", "SO", "TO",
    "TOE", "TOW", "WAS", "WOW",)
# For testing purposes,
# we install the standard dictionary here.

class TestCases(unittest.TestCase):
    def test_encode_case_1(self):
        inp = "AM"
        out = ".- --"
        self.assertEqual(hw2.encode(inp), out)

    def test_encode_case_2(self):
        inp = "CAN"
        out = "-.-. .- -."
        self.assertEqual(hw2.encode(inp), out)

    def test_encode_case_3(self):
        inp = "SEE"
        out = "... . ."
        self.assertEqual(hw2.encode(inp), out)

    def test_encode_case_4(self):
        inp = "GLOW"
        out = "--. .-.. --- .--"
        self.assertEqual(hw2.encode(inp), out)

    def test_decode_case_cat(self):
        inp = "-.-. .- -"
        out = "CAT"
        self.assertEqual(hw2.decode(inp), out)

    def test_decode_case_house(self):
        inp = ".... --- ..- ... ."
        out = "HOUSE"
        self.assertEqual(hw2.decode(inp), out)

    def test_decode_case_python(self):
        inp = ".--. -.-- - .... --- -."
        out = "PYTHON"
        self.assertEqual(hw2.decode(inp), out)

    def test_decode_case_knowledge(self):
        inp = "-.- -. --- .-- .-.. . -.. --. ."
        out = "KNOWLEDGE"
        self.assertEqual(hw2.decode(inp), out)

    def test_decode_case_question_mark(self):
        inp = "..---.--..."
        out = "?"
        self.assertEqual(hw2.decode(inp), out)

    def test_matches_case_1(self):
        inp = "-.-..--."
        out = ("CAN",)
        self.assertCountEqual(hw2.matches(inp), out)

    def test_matches_case_2(self):
        inp = "....."
        out = ("SEE", "HE", "IS",)
        self.assertCountEqual(hw2.matches(inp), out)

    def test_matches_case_3(self):
        inp = "................"
        out = ()
        self.assertCountEqual(hw2.matches(inp), out)

    def test_matches_case_4(self):
        inp = "----."
        out = ("ON", "TOE",)
        self.assertCountEqual(hw2.matches(inp), out)

if __name__ == "__main__":
    unittest.main()
