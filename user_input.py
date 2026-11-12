# User prompts when creating and updating pupils and classrooms for school
# Helen Connor Sørensen
# Created 12.11.2026

from datetime import date
from enums import Gender
from pupil import Pupil
from classroom import Classroom
from school import School


def ask_first_name(first_name=None):  # default value for order_name is None, otherwise it can be passed
    if first_name is None:
        first_name = str(input("Please give me your name:  "))
        return first_name
