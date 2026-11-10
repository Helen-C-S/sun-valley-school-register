# Create pupil class 5.11.2026

from datetime import date
from enums import Gender

MAX_NAME_LENGTH = 50


class Pupil:
    def __init__(self, first_name, last_name, birthday, gender, middle_name=None, allergies=None):
        self.__pupil_id = None # assigned by School
        self.__class_id = None # unassigned until placed
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_birthday(birthday)
        self.set_gender(gender)
        self.set_middle_name(middle_name)
        self.set_allergies(allergies)


    # setters
    def set_first_name(self, first_name):
        if not first_name or not first_name.strip():
            raise ValueError("First name cannot be empty")
        if len(first_name.strip()) > MAX_NAME_LENGTH:
            raise ValueError("First name cannot be longer than {} characters".format(MAX_NAME_LENGTH))
        self.__first_name = first_name.strip()

    def set_last_name(self, last_name):
        if not last_name or not last_name.strip():
            raise ValueError("Last name cannot be empty")
        if len(last_name.strip()) > MAX_NAME_LENGTH:
            raise ValueError("Last name cannot be longer than {} characters".format(MAX_NAME_LENGTH))
        self.__last_name = last_name.strip()

    def set_birthday(self, birthday):
        if isinstance(birthday, str):
            birthday = date.fromisoformat(birthday) # raises ValueError on bad format
        if birthday >= date.today():
            raise ValueError("Birthday cannot be earlier than today's date")
        self.__birthday = birthday

    def set_gender(self, gender):
        if not isinstance(gender, Gender):
            raise ValueError("Gender must be either MALE, FEMALE or NONBINARY")
        self.__gender = gender

    def set_middle_name(self, middle_name):
        if middle_name is None or not middle_name.strip():
            self.__middle_name = None
        elif len(middle_name.strip()) > MAX_NAME_LENGTH:
            raise ValueError("Middle name cannot be longer than {} characters".format(MAX_NAME_LENGTH))
        else:
            self.__middle_name = middle_name

    def set_allergies(self, allergies):
        if allergies is None or not allergies.strip():
            self.__allergies = None
        self.__allergies = allergies

    # pupil_id added to pupil objects before pupil appended to pupils
    def set_pupil_id(self, pupil_id):
        try:
            pupil_id = int(pupil_id) # 10.11.2026
        except ValueError:
            raise ValueError("pupil_id must be a whole number")
        if pupil_id < 1:
            raise ValueError("pupil_id must greater than 1")
        self.__pupil_id = pupil_id

    # getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_birthday(self):
        return self.__birthday

    def get_gender(self):
        return self.__gender

    def get_middle_name(self):
        return self.__middle_name

    def get_allergies(self):
        return self.__allergies

    def get_age(self):
        today = date.today()
        b = self.__birthday
        return today.year - b.year - ((today.month, today.day) < (b.month, b.day))

    def has_allergies(self):
        return self.__allergies is not None

    def get_pupil_id(self):
        return self.__pupil_id

    # to print the contents of the object
    def __str__(self):
        return (f"First name: {self.__first_name}, Last name: {self.__last_name},"
                f"Birthday:  {self.__birthday}, Gender: {self.__gender.value},"
                f"\nMiddle Name: {self.__middle_name}, Allergies: {self.__allergies}")

