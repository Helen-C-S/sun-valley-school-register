# scripts to test that classes and data structures are working
import user_input
import submenus
from enums import Gender
from enums import Letter
from pupil import Pupil
from classroom import Classroom
from datetime import date
from school import School

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
# c = Classroom("7A", "Katrina", 25)
# print(c)
# #bad examples
# # no grade
# try:
#     c = Classroom("A", "Katrina", 25)
# except ValueError as e:
#     print("Expected error:", e)
# #no letter
# try:
#     c = Classroom("10", "Katrina", 25)
# except ValueError as e:
#     print("Expected error:", e)
# # grade outside range
# try:
#     c = Classroom("12A", "Katrina", 25)
# except ValueError as e:
#     print("Expected error:", e)
# # not a valid letter
# try:
#     c = Classroom("7F", "Katrina", 25)
# except ValueError as e:
#     print("Expected error:", e)
# # Negative grade
# try:
#     c = Classroom("-1A", "Katrina", 25)
# except ValueError as e:
#     print("Expected error:", e)
# # letter grade
# try:
#     c = Classroom("xA", "Katrina", 25)
# except ValueError as e:
#     print("Expected error:", e)

# # add pupil to school 8.11.2026
# p1 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE)
# p2 = Pupil("Jens", "Rasmussen", date(2014, 7, 26), Gender.MALE)
# school = School()
# school.add_pupil(p1)
# school.add_pupil(p2)
# school.read_pupils()
# # add classroom to school 8.11.2026
# c1 = Classroom("7A", "Katrina", 25)
# c2 = Classroom("0B", "Christina", 25)
# school.add_classroom(c1)
# school.add_classroom(c2)
# school.read_classrooms()
#
# # add_classroom, test input validation 10.11.2026
# # avoid duplicate classrooms
# c3 = Classroom("7A", "Marianne", 20)
# try:
#     school.add_classroom(c3)
# except ValueError as e:
#     print("Expected error:", e)
#
# # test find classroom method, 10.11.2026
# print(school.find_classroom("7A"))     # the classroom
# print(school.find_classroom("9E"))     # None


# # add pupil to school 10.11.2026
# p1 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE)
# p2 = Pupil("Jens", "Rasmussen", date(2014, 7, 26), Gender.MALE)
# school = School()
# school.add_pupil(p1)
# school.add_pupil(p2)
# school.read_pupils()
# print(p1.get_pupil_id())
# print(p2.get_pupil_id())
#
# # check pupil_id and next_pupil_id update appropriately if next_pupil_id is set from outside
# school.set_next_pupil_id(10)
# p3 = Pupil("Sophie", "Larsen", date(2014, 2, 8), Gender.NONBINARY)
# school.add_pupil(p3)
# print(p3.get_pupil_id())
# print(school.get_next_pupil_id())
#
#
# # test bad pupil_ids 10.11.2026
# school=School()
# try:
#     school.set_next_pupil_id("abc")
# except ValueError as e:
#     print(e)
# try:
#     school.set_next_pupil_id(0)
# except ValueError as e:
#     print(e)
# try:
#     school.set_next_pupil_id(-1)
# except ValueError as e:
#     print(e)

def test_pupil_id_autocorrect():# 10.11.2026
    p1 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F)
    p2 = Pupil("Jens", "Rasmussen", date(2014, 7, 26), Gender.M)
    school = School()
    school.add_pupil(p1)
    school.add_pupil(p2)
    print(p1.get_pupil_id())
    print(p2.get_pupil_id())
    school.set_next_pupil_id(1)
    p3 = Pupil("Sophie", "Larsen", date(2014, 2, 8), Gender.N)
    school.add_pupil(p3)
    print(p3.get_pupil_id())
    print(school.get_next_pupil_id())

#test_pupil_id_autocorrect()

# test the user input for build pupil 12.11.2026
def test_name_input():
    first_name = user_input.ask_first_name()
    middle_name = user_input.ask_middle_name()
    last_name = user_input.ask_last_name()
    print(first_name, middle_name, last_name)
#test_name_input()

# test the user input for Gender 12.11.2026
def test_gender_input():
    gender = user_input.ask_gender()
    print(gender.value)
#test_gender_input()

# test birthday 13.11.2026. Tested with valid and invalid dates, including 31 Feb
def test_birthday():
    birthday = user_input.ask_birthday()
    print(birthday)
#test_birthday()

# test  allergies 13.11.2026
def test_ask_allergies():
    allergies = user_input.ask_allergies()
    print(allergies)
#test_ask_allergies()

# test build_pupil 13.11.2026 # good and bad cases tested
def test_build_pupil():
    school = School()
    p=submenus.build_pupil(school)
    school.add_pupil(p) # assigns pupil_id
    print(p)
#test_build_pupil()

# Input validation for name input in user_input updated 13.10.2026
# first and last names must be at least two letters
# Test name input again 13.10.2026
#test_name_input()

# build_pupil and add_pupil tested from main 13.11.2026

# test school.read_all_pupils 13.11.2026
def test_read_all_pupils():
    school = School()
    submenus.show_all_pupils(school)
    p1 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F)
    p2 = Pupil("Jens", "Rasmussen", date(2014, 7, 26), Gender.M)
    school.add_pupil(p1)
    school.add_pupil(p2)
    submenus.show_all_pupils(school)
#test_read_all_pupils()

# show_all_pupils tested from main 13.11.2026

# test refactored validators for pupil class 13.11.2026
def test_validate_creating_pupil():
    school = School()
    try:
        # good cases
        p1 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F)
        print(p1)
        p2 = Pupil("Jens", "Rasmussen", date(2014, 7, 26), Gender.M)
        print(p2)
        # bad cases
        #p3 = Pupil("A", "Hansen", date(2014, 3, 2), Gender.F)
        #p4 = Pupil(("A"*51), "Hansen", date(2014, 3, 2), Gender.F)
        #p5 = Pupil("Jens", "", date(2014, 7, 26), Gender.M)
        # test optional text attributes
        p6 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F, middle_name="Marie")
        print(p6)
        # other cases
        # p7 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F, middle_name="")
        # print(p7)
        # p8 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F, middle_name=("M"*51))
        # print(p8)
        # test allergies
        # p9 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F, allergies="Peanuts")
        # print(p9)
        # p10 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F, allergies="")
        # print(p10)
        # test validate date
        #p11 = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F)
        #print(p11)
        #p12 = Pupil("Anna", "Hansen", date(2014, 3, 35), Gender.F)
        #p12 = Pupil("Anna", "Hansen", date(2028, 3, 15), Gender.F)
        #print(p12)
        # test validate gender
        # p13 = Pupil("Leo", "Schmidt", date(2014, 3, 15), Gender.N)
        # print(p13)
        # # test validate gender, bad case
        #p14 = Pupil("Leo", "Schmidt", date(2014, 3, 15), Gender.L)
        p14 = Pupil("Leo", "Schmidt", date(2014, 3, 15), "L")
        # print(p14)
    except ValueError as e:
        print(e)
#test_validate_creating_pupil()

# updated pupil_id re-factored validation 13.11.2026
#test_pupil_id_autocorrect()

# test find pupil functionality (supports update and delete) 13.11.2026
def test_find_pupil(test_id):
    school = School()
    p1=Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F)
    school.add_pupil(p1)
    p2 = school.find_pupil(test_id)
    print(p2)
test_find_pupil(1)

# test delete_pupil 13.11.2026
def test_delete_pupil(test_id):
    school = School()
    p1=Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.F)
    p2=Pupil("Leo", "Schmidt", date(2014, 3, 15), Gender.N)
    school.add_pupil(p1)
    school.add_pupil(p2)
    submenus.display_all_pupils(school)
    school.delete_pupil(test_id)
    print("")
    submenus.display_all_pupils(school)
#test_delete_pupil(1)

# read and delete include school.has_pupils() check 14.11.2026
# Delete functionality added and tested with good and bad cases from menus

# test get_sorted_pupils functionality in school. Only last name sort available at the moment. 14.11.2026
def test_sort_pupils():
    school = School()
    print("--new test--")
    try:
        submenus.display_sorted_pupils(school)
    except ValueError as e:
        print(e)
    p1 = Pupil("Anna", "Rasmussen", date(2014, 3, 2), Gender.F)
    p2 = Pupil("Leo", "Larsen", date(2014, 3, 15), Gender.N)
    school.add_pupil(p1)
    school.add_pupil(p2)
    print("--print all pupils unsorted--")
    submenus.display_all_pupils(school)
    print("--print pupils sorted--")
    submenus.display_sorted_pupils(school)
#test_sort_pupils()
# also tested from menus 14.11.2026

# test_update_pupil functionality 14.11.2026
def test_update_pupil():
    school = School()
    print("--new test--")
    p1 = Pupil("Anna", "Rasmussen", date(2014, 3, 2), Gender.F)
    p2 = Pupil("Leo", "Larsen", date(2014, 3, 15), Gender.N)
    school.add_pupil(p1)
    school.add_pupil(p2)
    print("--print all pupils unsorted--")
    submenus.display_all_pupils(school)
    school.update_pupil(1, "first_name", "Annenew")
    print("--print updated pupil--")
    print(p1)
    print("--print all pupils--")
    submenus.display_all_pupils(school)
    try: # try an invalid pupil_id
        school.update_pupil(6, "first_name", "Anneagain")
        print(p1)
    except ValueError as e:
        print(e) # it passed without error, but the update does not take place. Catch in submenus
    try: # try a valid last_name
        school.update_pupil(1, "last_name", "Rasmussen")
        print(p1)
    except ValueError as e:
        print(e)
    try: # try invalid last_name
        school.update_pupil(1, "last_name", ("Rasmussen"*10))
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try a valid middle_name
        school.update_pupil(1, "middle_name", "Marie")
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try invalid last_name
        school.update_pupil(1, "middle_name", ("Marie" * 11))
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try middle_name None
        school.update_pupil(1, "middle_name", "")
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try valid date
        school.update_pupil(1, "birthday", "2012-10-24")
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try invalid date
        school.update_pupil(1, "birthday", "2012-10-35")
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try valid gender
        school.update_pupil(1, "gender", Gender.N)
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try invalid gender
        school.update_pupil(1, "gender", "L")
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try invalid date
        school.update_pupil(1, "birthday", "2012-10-35")
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try valid allergies
        school.update_pupil(1, "allergies", "Peanuts")
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try invalid allergies
        school.update_pupil(1, "allergies", ("L"*51))
        print(p1)
    except ValueError as e:
        print(e)
    try:  # try allergies None
        school.update_pupil(1, "allergies", "")
        print(p1)
    except ValueError as e:
        print(e)
#test_update_pupil()

# test edit_pupil
def test_edit_pupil():
    school = School()
    print("--new test--")
    p1 = Pupil("Anna", "Rasmussen", date(2014, 3, 2), Gender.F)
    p2 = Pupil("Leo", "Larsen", date(2014, 3, 15), Gender.N)
    school.add_pupil(p1)
    school.add_pupil(p2)
    print("--print all pupils unsorted--")
    submenus.display_all_pupils(school)
    submenus.edit_pupil(school)
test_edit_pupil()

