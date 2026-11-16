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
            if len(first_name) < 2:
                raise ValueError
            return first_name
        except ValueError:
            print("The pupil's name must contain at least two letters")

def ask_middle_name(): # no middle name is converted to None in the validation
    middle_name = input("What is the pupil's middle name (Please push Enter, if none):  ")
    return middle_name

def ask_last_name():
    while True:
        try:
            last_name = input("What is the pupil's last name:  ")
            if len(last_name) < 2:
                raise ValueError
            return last_name
        except ValueError:
            print("The pupil's last name must contain at least two letters")

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
            month = input("Month (1-12):  ")
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
            day = input("Day (1-31):  ")
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
        try:
            if int(choice) < 1:
                raise IndexError
            field = items[int(choice) - 1]
            return field
        except IndexError:
            print("Please choose a number between 1 and", len(items))
        except ValueError:
            print("Invalid choice. Please choose a number between 1 and", len(items))
