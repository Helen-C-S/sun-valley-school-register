# create class School 8.11.2026from datetime import date
# from enums import Gender
# from pupil import Pupil
# from classroom import Classroom



class School:
    def __init__(self):
        self.__pupils = []
        self.__classrooms = []
        self.__next_pupil_id = None


    # CREATE
    def add_pupil(self, pupil):
        self.__pupils.append(pupil)

    def add_classroom(self, classroom):
        self.__classrooms.append(classroom)

    # READ
    def read_pupils(self):
        for pupil in self.__pupils:
            print(pupil)

    def read_classrooms(self):
        for classroom in self.__classrooms:
            print(classroom)