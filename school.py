# create class School 8.11.2026
import datetime
import pupil
import validators
from enums import Gender
from pupil import Pupil
from classroom import Classroom



class School:
    def __init__(self):
        self.__pupils = []
        self.__classrooms = []
        self.__next_pupil_id = 1

    # PUPILS CREATE
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


    def get_next_pupil_id(self):
        return self.__next_pupil_id

    # RETRIEVE PUPILS
    def has_pupils(self):
        pupils = self.__pupils
        if not pupils:
            return False
        else:
            return True

    def get_pupils(self):
        return list(self.__pupils)

    # UPDATE
    def update_pupil(self, pupil_id, field, new_value):
        p = self.find_pupil(pupil_id)
        if p is not None:
            match field:
                case "first_name":
                    p.set_first_name(new_value)
                case "last_name":
                    p.set_last_name(new_value)
                case "birthday":
                    p.set_birthday(new_value)
                case "gender":
                    p.set_gender(new_value)
                case "middle_name":
                    p.set_middle_name(new_value)
                case "allergies":
                    p.set_allergies(new_value)
                case _:
                    raise ValueError("Unknown field")
            return True # flag to display in submenus that update accepted
        return False # flag for the display in submenus that pupil_id not found
    #has_pupils functionality neccessary for READ, UPDATE, CREATE and SORT

    # DELETE PUPILS
    def delete_pupil(self, pupil_id):
        pupil = self.find_pupil(pupil_id)
        if pupil is None:
            return False
        self.__pupils.remove(pupil)
        return True

    #SORT PUPILS
    def get_sorted_pupils(self):
        return sorted(self.__pupils, key=lambda pupil: pupil.get_last_name())

    # FIND PUPIL
    def find_pupil(self, pupil_id):
        pupil_id = int(pupil_id) # protection against zero-padded inputs
        for pupil in self.__pupils:
            if pupil.get_pupil_id() == pupil_id:
                return pupil
        return None

    # CREATE CLASSROOMS
    def add_classroom(self, classroom):
        if self.find_classroom(classroom.get_class_id()) is not None:
            raise ValueError(f"Classroom {classroom.get_class_id()} already exists")
        self.__classrooms.append(classroom)
        print(f"Classroom {classroom.get_class_id()} is now added to the school.")

    # RETRIEVE CLASSROOMS
    def read_classrooms(self):
        return list(self.__classrooms)

    # FIND CLASSROOM
    def find_classroom(self, class_id):
        for classroom in self.__classrooms:
            if classroom.get_class_id() == class_id:
                return classroom
        return None


    # SAVE/LOAD FUNCTIONS
    # save pupils
    def save_pupils(self):
        if not self.__pupils:  # if the orders list is empty
            print("No pupils to save")
            return
        filename = datetime.datetime.now().strftime("data/pupils_%Y%m%d_%H%M%S.txt")
        with open(filename, "w") as f:
            for p in self.__pupils:
                f.write(f"{p.get_pupil_id():04d};{p.get_class_id()};" # pupil_id zero-pad
                        f"{p.get_first_name()};{p.get_last_name()};{p.get_middle_name()}; "
                        f"{p.get_gender().name};{p.get_allergies()}\n")
        print("Pupils saved to", filename)
