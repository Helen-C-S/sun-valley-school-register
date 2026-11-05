# Create pupil class 5.11.2026

from datetime import date
from enums import Gender


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
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_birthday(self, birthday):
        self.__birthday = birthday

    def set_gender(self, gender):
        self.__gender = gender

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_allergies(self, allergies):
        self.__allergies = allergies

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

