# Create pupil class 5.11.2026

from datetime import date
from enums import Gender
import validators


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
        self.__first_name = validators.validate_name(first_name, "First name")

    def set_last_name(self, last_name):
        self.__last_name = validators.validate_name(last_name, "Last name")


    def set_birthday(self, birthday):
        self.__birthday = validators.validate_date(birthday, "Birthday")

    def set_gender(self, gender):
        self.__gender = validators.validate_gender(gender)

    def set_middle_name(self, middle_name):
        self.__middle_name = validators.validate_optional_text(middle_name, "Middle name")

    def set_allergies(self, allergies):
        self.__allergies = validators.validate_optional_text(allergies, "Allergies")


    # pupil_id come from school.py
    def set_pupil_id(self, pupil_id):
        self.__pupil_id = pupil_id

    # class_id comes from classroom.py added 17.11.2026
    def set_class_id(self, class_id):
        self.__class_id = class_id

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

    def get_class_id(self):
        return self.__class_id

    # to print the contents of the object
    def __str__(self):
        return (f"pupil_id: {self.__pupil_id}, classroom: {self.__class_id} "
                f"\nFirst name: {self.__first_name}, Middle Name: {self.__middle_name}, Last name: {self.__last_name},"
                f"\nBirthday:  {self.__birthday}, Gender: {self.__gender.value}, Allergies: {self.__allergies}")

