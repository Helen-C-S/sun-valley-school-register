# scripts to test that classes and data structures are working
from enums import Gender
from enums import Letter
from pupil import Pupil
from classroom import Classroom
from datetime import date

# # test enums 4.11.2026
# gender = Gender.FEMALE
# print(gender.name, gender.value)
# letter = Letter.A
# print(letter.name, letter.value)


# test pupils 5.11.2026
#p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE)
#print(p.get_first_name(), p.get_middle_name(), p.get_last_name(), p.get_birthday(), p.get_gender().value, p.get_allergies())


# test classrooms 7.11.2026
#c = Classroom("7A", "Katrina", 25)
#print(c.get_class_id(), c.get_teacher(), c.get_max_cap())

# # start adding validation and testing validation for pupil class 7.11.2026
# # test empty first name
# #p = Pupil("", "Hansen", date(2014, 3, 2), Gender.FEMALE)
# # test first name with only spaces
# #p = Pupil("  ", "Hansen", date(2014, 3, 2), Gender.FEMALE)
# # test empty last name
# #p = Pupil("Anna", "", date(2014, 3, 2), Gender.FEMALE)
# # test last name with only spaces
# #p = Pupil("Anna", " ", date(2014, 3, 2), Gender.FEMALE)
#
# # the good case 7.11.2026
# p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE)
# print(p)
#
# # try bad date format 7.11.2026
# try:
#     p = Pupil("Anna", "Hansen", "2014-3-2", Gender.FEMALE)
# except ValueError as e:
#     print("Expected error:", e)
#
# # try bad gender format
# try:
#     p = Pupil("Anna", "Hansen", date(2014, 3, 2), "F")
# except ValueError as e:
#     print("Expected error:", e)
#
# # try to get the age
# p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE)
# print(p.get_age(), "years")
#
# # validate has_allergies 7.11.2026
# # "has allergies" example
# p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE, allergies="cats")
# print("Has allergies:", p.has_allergies())
# # has no allergies example
# p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE)
# print("Has allergies:", p.has_allergies())
# # allergies coded as spaces
# p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE, allergies="  ")
#
# # test name length validation 7.11.2026
# # good case
# p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE)
# print(p)
# # bad first name
# try:
#     p = Pupil("A"*51, "Hansen", date(2014, 3, 2), Gender.FEMALE)
# except ValueError as e:
#     print("Expected error:", e)
# # bad last name
# try:
#     p = Pupil("Anna", "H"*51, date(2014, 3, 2), Gender.FEMALE)
# except ValueError as e:
#     print("Expected error:", e)
# # bad middle name
# try:
#     p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE, middle_name=("E"*51))
# except ValueError as e:
#     print("Expected error:", e)
#
#

# # test input validation for Classroom 7.11.2026
# # good example
# c = Classroom("7A", "Katrina", 25)
# print(c)
# # Example of absent teacher name
# try:
#     c = Classroom("7A", "", 25)
# except ValueError as e:
#     print("Expected error:", e)
# # Example of classroom capacity outside range
# try:
#     c = Classroom("7A", "Katrina", "abc")
# except ValueError as e:
#     print("Expected error:", e)
# try:
#     c = Classroom("7A", "Katrina", 50)
# except ValueError as e:
#     print("Expected error:", e)
# try:
#     c = Classroom("7A", "Katrina", 0)
# except ValueError as e:
#     print("Expected error:", e)
# try:
#     c = Classroom("7A", "Katrina", 0)
# except ValueError as e:
#     print("Expected error:", e)
#

# test that class is follows grade followed by single letter 7.11.2026
# good example
c = Classroom("7A", "Katrina", 25)
print(c)
#bad examples
# no grade
try:
    c = Classroom("A", "Katrina", 25)
except ValueError as e:
    print("Expected error:", e)
#no letter
try:
    c = Classroom("10", "Katrina", 25)
except ValueError as e:
    print("Expected error:", e)
# grade outside range
try:
    c = Classroom("12A", "Katrina", 25)
except ValueError as e:
    print("Expected error:", e)
# not a valid letter
try:
    c = Classroom("7F", "Katrina", 25)
except ValueError as e:
    print("Expected error:", e)
# Negative grade
try:
    c = Classroom("-1A", "Katrina", 25)
except ValueError as e:
    print("Expected error:", e)
# letter grade
try:
    c = Classroom("xA", "Katrina", 25)
except ValueError as e:
    print("Expected error:", e)