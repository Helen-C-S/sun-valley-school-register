# create class School 8.11.2026
from datetime import date

import validators
from enums import Gender
from pupil import Pupil
from classroom import Classroom



class School:
    def __init__(self):
        self.__pupils = []
        self.__classrooms = []
        self.__next_pupil_id = 1

    # CREATE 8.11.2026, pupil_id counter added 10.11.2026
    def add_pupil(self, pupil):
        new_id = self.get_next_pupil_id() # pupil_id only goes through getter/setters
        pupil.set_pupil_id(new_id)
        new_id += 1
        self.set_next_pupil_id(new_id)
        self.__pupils.append(pupil)


    def set_next_pupil_id(self, next_pupil_id): # required for loading and testing
        self.__next_pupil_id = validators.validate_int_range(next_pupil_id, "next_pupil_id", 1)
        # auto-correct: never reuse an existing pupil_id
        if self.__pupils: # auto-correct does not run if pupils list empty
            existing_ids = []
            for p in self.__pupils:
                existing_ids.append(p.get_pupil_id())
            max_existing_id = max(existing_ids)
            if next_pupil_id <= max_existing_id:
                print(f"next_pupil_id {next_pupil_id} already in use, set to {max_existing_id + 1}")
                next_pupil_id = max_existing_id + 1
        self.__next_pupil_id = next_pupil_id


    # See if classroom already exists 10.11.2026
    def find_classroom(self, class_id):
        for classroom in self.__classrooms:
            if classroom.get_class_id() == class_id:
                return classroom
        return None


    # CREATE and prevent duplication of classrooms
    def add_classroom(self, classroom):
        if self.find_classroom(classroom.get_class_id()) is not None:
            raise ValueError(f"Classroom {classroom.get_class_id()} already exists")
        self.__classrooms.append(classroom)
        print(f"Classroom {classroom.get_class_id()} is now added to the school.")


    # READ
    # getters for pupils list
    def get_pupils(self):
        return list(self.__pupils)

    def read_classrooms(self):
        for classroom in self.__classrooms:
            print(classroom)

    def get_next_pupil_id(self):
        return self.__next_pupil_id