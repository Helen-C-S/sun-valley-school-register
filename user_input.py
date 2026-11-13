# User prompts when creating and updating pupils and classrooms for school
# User input is validated to check if data can be turned into right type
# if not, then that question is asked again
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

def ask_middle_name(): # no middle name is caught in the validation
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

def ask_birthday():
    print("When was the pupil born?")
    # collect year
    while True:
        try:
            year = input("Year (YYYY):  ")
            if len(year) != 4:
                raise ValueError
            year = int(year)
            break # valid year input
        except ValueError:
            print("Please enter numbers in YYYY format")
    # collect month
    while True:
        try:
            month = input("Month:  ")
            if len(month) > 2:
                raise ValueError
            month = int(month)
            if month not in range(1, 13):
                raise ValueError
            break # valid month collected
        except ValueError:
            print("Please enter month in numbers (1-12)")
    # collect day
    while True:
        try:
            day = input("Day:  ")
            if len(day) > 2:
                raise ValueError
            day = int(day)
            if day not in range(1, 32):
                raise ValueError
        except ValueError:
            print("Please enter day in numbers (1-31)")
            continue # ask for the date again
        # assemble date and check for valid date combinations.
        try:
            birthday = date(year, month, day)
            return birthday
        except ValueError as e:
            print(f"That date does not exist ({e}). Please enter the date again")

def ask_allergies(): # no allergies is caught in the validation
    allergies = input("Does the pupil have any allergies (Please push Enter, if none):  ")
    return allergies
