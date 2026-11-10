# Create classroom class 7.11.2026
from enums import Letter

MAX_NAME_LENGTH = 50
ABS_MAX_CAP = 35
MIN_GRADE = 0
MAX_GRADE = 10


class Classroom:
    def __init__(self, class_id, teacher, max_cap):
        self.set_class_id(class_id)
        self.set_teacher(teacher)
        self.set_max_cap(max_cap)


    # setters
    def set_class_id(self, class_id):
        class_id = str(class_id).strip().upper() # input converted to upper case, any spaces removed
        if len(class_id) < 2 or not class_id[-1].isalpha():
            raise ValueError("Class ID must be a grade followed by a letter")
        grade_part = class_id[:-1]
        try:
            grade = int(grade_part)
        except ValueError:
            raise ValueError("Grade must be a whole number")
        letter_part = class_id[-1]

        if grade < MIN_GRADE or grade > MAX_GRADE:
            raise ValueError("Grade must be between {} and {}".format(MIN_GRADE, MAX_GRADE))
        if letter_part not in Letter.__members__:
            raise ValueError("Letter must be one of {}".format(", ".join(Letter.__members__)))
        self.__class_id = class_id

    def set_teacher(self, teacher):
        if not teacher or not teacher.strip():
            raise ValueError("Teacher cannot be empty")
        if len(teacher) > MAX_NAME_LENGTH:
            raise ValueError("Teacher cannot be longer than {} characters".format(MAX_NAME_LENGTH))
        self.__teacher = teacher


    def set_max_cap(self, max_cap):
        if max_cap is None or str(max_cap).strip() == "":
            raise ValueError("Max Cap cannot be empty")
        max_cap = int(max_cap)
        if max_cap < 1:
            raise ValueError("There must be at least 1 pupil")
        if max_cap > ABS_MAX_CAP:
            raise ValueError("The classroom can not be bigger than {} pupils or the union will complain".format(ABS_MAX_CAP))
        self.__max_cap = max_cap

    # getters
    def get_class_id(self):
        return self.__class_id

    def get_teacher(self):
        return self.__teacher

    def get_max_cap(self):
        return self.__max_cap

    # make the text nice
    def __str__(self):
        return f"class_id: {self.__class_id}, Teacher:  {self.__teacher}, Maximum Capacity: {self.__max_cap}"

