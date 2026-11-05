# scripts to test that classes and data structures are working
from enums import Gender
from enums import Letter
from pupil import Pupil
from datetime import date

# # test enums 4.11.2026
# gender = Gender.FEMALE
# print(gender.name, gender.value)
# letter = Letter.A
# print(letter.name, letter.value)


# test pupils
p = Pupil("Anna", "Hansen", date(2014, 3, 2), Gender.FEMALE)
print(p.get_first_name(), p.get_middle_name(), p.get_last_name(), p.get_birthday(), p.get_gender().value, p.get_allergies())