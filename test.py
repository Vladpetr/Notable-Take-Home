import unittest
from code import *


class MyTestCase(unittest.TestCase):
    def test_original(self):
        """
        Checks the original example mentioned in the prompt.
        """
        example = "Patient presents today with several issues. Number one BMI has increased by 10% " \
                  "since their last visit number next patient reports experiencing dizziness several times " \
                  "in the last two weeks. Number next patient has a persistent cough that hasn’t " \
                  "improved for last 4 weeks Number next patient is taking drug number five several " \
                  "times a week"

        result = "Patient presents today with several issues.\n" \
                 "1. BMI has increased by 10% since their last visit\n" \
                 "2. Patient reports experiencing dizziness several times in the last two weeks.\n" \
                 "3. Patient has a persistent cough that hasn’t improved for last 4 weeks\n" \
                 "4. Patient is taking drug number five several times a week"

        test = NoteTransformation(example)
        self.assertEqual(test.transform(), result, "Incorrect transformation")

    def test_no_list(self):
        """
        Checks if the input has no "Number ..." phrases.
        According to code behavior, the algorithm should parse the whole text
        without making any changes to the original input.
        """
        example = "Patient presents today with several issues. BMI has increased by 10% " \
                  "since their last visit. Patient reports experiencing dizziness several times " \
                  "in the last two weeks. Patient has a persistent cough that hasn’t " \
                  "improved for last 4 weeks. Patient is taking drug several " \
                  "times a week"

        result = example

        test = NoteTransformation(example)
        self.assertEqual(test.transform(), result, "Incorrect transformation")

    def test_next_first(self):
        """
        Checks if the input has "Number next" first before declaring the value of n.
        According to code behavior, the algorithm should parse the phrase "number next"
        without turning it into the element of a numbered list
        """
        example = "Patient presents today with several issues. Number next BMI has increased by 10% " \
                  "since their last visit number two patient reports experiencing dizziness several times " \
                  "in the last two weeks. Number next patient has a persistent cough that hasn’t " \
                  "improved for last 4 weeks Number next patient is taking drug number five several " \
                  "times a week"

        result = "Patient presents today with several issues. Number next BMI has increased by 10%" \
                 " since their last visit\n" \
                 "1. \n" \
                 "2. Patient reports experiencing dizziness several times in the last two weeks.\n" \
                 "3. Patient has a persistent cough that hasn’t improved for last 4 weeks\n" \
                 "4. Patient is taking drug number five several times a week"
        test = NoteTransformation(example)

        self.assertEqual(test.transform(), result, "Incorrect transformation")


unittest.main()

