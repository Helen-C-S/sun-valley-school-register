# User prompts when creating and updating pupils and classrooms for school
# User input is validated to check if data can be turned into right type
# if not, then that question is asked again
# Helen Connor Sørensen
# Created 12.11.2026

from datetime import date
import validators
from enums import Gender

PUPIL_FIELDS = ("first_name", "last_name", "middle_name", "birthday", "gender", "allergies")

def ask_first_name():
    while True:
        try:
            first_name = input("What is the pupil's first name:  ")
            validators.validate_name(first_name, "First name")
            return first_name
        except ValueError as e:
            print(e)

def ask_middle_name(): # no middle name is converted to None in the validation
    while True:
        try:
            middle_name = input("What is the pupil's middle name (Please push Enter, if none):  ")
            validators.validate_optional_text(middle_name, "Middle name", False)
            return middle_name
        except ValueError as e:
            print(e)

def ask_last_name():
    while True:
        try:
            last_name = input("What is the pupil's last name:  ")
            validators.validate_name(last_name, "Last name")
            return last_name
        except ValueError as e:
            print(e)


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
    while True:
        print("When was the pupil born?")
        while True: # collect year
            try:
                year = input("Year (YYYY):  ")
                year = validators.validate_year(year)
                break
            except ValueError as e:
                print(e)
        while True:
            try: # collect month
                month = input("Month (1-12):  ")
                month = validators.validate_int_range(month, "The month", 1, 12)
                break # valid month collected
            except ValueError as e:
                print(e)
        while True: # collect day
            try:
                day = input("Day (1-31):  ")
                day = validators.validate_int_range(day, "The day", 1, 31)
                break
            except ValueError as e:
                print(e)
            # assemble date and check for valid date combinations.
        try:
            birthday = date(year, month, day)
            birthday = validators.validate_date(birthday, "Date of birth")
            return birthday
        except ValueError as e:
            print(e)

def ask_allergies(): # no allergies is caught in the validation
    while True:
        try:
            allergies = input("Does the pupil have any allergies (Please push Enter, if none):  ")
            validators.validate_optional_text(allergies, "Allergies", True)
            return allergies
        except ValueError as e:
            print(e)

def ask_which_pupil(label, max_id=None):
    while True:
        try:
            pupil_id = input(f"Which pupil would you like to {label} (Please enter pupil_id)?:  ")
            pupil_id = validators.validate_int_range(pupil_id, 'pupil_id',1, max_id)
            return pupil_id
        except ValueError as e:
            print(e)

def ask_confirmation(label):
    confirmation = input(f"Do you wish to {label.lower()}? Y/N:  ")
    if confirmation.strip().upper() == "Y":
        print(f"{label.capitalize()} confirmed")
        return True
    else:
        print(f"{label.capitalize()} cancelled")
        return False

def ask_pupil_field(label):
    print("")
    print(f"Which pupil information field would you like to {label.lower()}?:  ")
    items = list(PUPIL_FIELDS)
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.replace('_',' ').capitalize()}")
    while True:
        choice = input("Which choice would you like to make?  ")
        number = validators.validate_int_range(choice, "The choice", 1, len(items))
        return items[number - 1]