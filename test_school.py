# scripts to test that classes and data structures are working
from enums import Gender
from enums import Letter

# test enums
gender = Gender.FEMALE
print(gender.name, gender.value)
letter = Letter.A
print(letter.name, letter.value)