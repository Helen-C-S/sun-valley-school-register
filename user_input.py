# User prompts when creating and updating pupils and classrooms for school
# Helen Connor Sørensen
# Created 12.11.2026

from datetime import date
from enums import Gender
from pupil import Pupil
from classroom import Classroom
from school import School


def ask_first_name():
    first_name = input("What is the pupil's first name:  ")
    return first_name

def ask_middle_name(): # no middle name is caught in the setter
    middle_name = input("What is the pupil's middle name (Please push Enter, if none):  ")
    return middle_name

def ask_last_name():
    last_name = input("What is the pupil's last name:  ")
    return last_name

def ask_gender():
    while True:
        print("What is the gender of the pupil?")
        answer = input("Choices are Female, Male or Non-binary (F/M/N):  ")
        try:
            gender = Gender[answer.strip().upper()]
            return gender
        except KeyError:
            print("Please enter either F, M or N")