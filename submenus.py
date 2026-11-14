# Options for the pupils and classrooms menus, as well as registering pupils
# Belongs to Sun Valley School
# Created 12.11.2026

from datetime import date
from enums import Gender
from pupil import Pupil
from classroom import Classroom
from school import School
import user_input

def pupil_menu(school):
    while True:
        print("")
        print("This is Sun Valley's register of pupils.")
        print("1. Register new pupil")
        print("2. See list of all enrolled pupils")
        print("3. Update personal details for a pupil")
        print("4. Delete a pupil")
        print("5. Sort pupils")
        print("6. Find pupils who do not have a classroom")
        print("7. Place a pupil in a classroom or change classroom")
        print("0. Back to the main menu")
        choice = input("Which choice would you like to make?  ")

        match choice:
            case "1": # register new pupil
                p = build_pupil(school) # in this script, collects user input
                if p is not None:
                    school.add_pupil(p)
                    print(f"Registered: {p}")
            case "2": # retrieve all pupils
                display_all_pupils(school)
            case "3":
                continue
            case "4": # delete pupuil
                remove_pupil(school)
            case "5":
                display_sorted_pupils(school)
            case "6":
                continue
            case "7":
                continue
            case "0":
                print("Returning to main menu...")
                return          # back to the main menu
            case _:
                print("Invalid choice")

def classroom_menu(school):
    while True:
        print("")
        print("This is Sun Valley's register of classes.")
        print("1. Register new class")
        print("2. See list of classes in the school")
        print("3. Update the details for a class")
        print("4. Delete a class")
        print("5. Sort classes")
        print("6. Show pupils in a class")
        print("0. Back to the main menu")
        choice = input("Which choice would you like to make?  ")

        match choice:
            case "1":
                continue
            case "2":
                continue
            case "3":
                continue
            case "4":
                continue
            case "5":
                continue
            case "6":
                continue
            case "0":
                print("Returning to main menu...")
                return          # back to the main menu
            case _:
                print("Invalid choice")

# CREATE PUPIL
def build_pupil(school):
    first_name = user_input.ask_first_name()
    middle_name = user_input.ask_middle_name()
    last_name = user_input.ask_last_name()
    birthday = user_input.ask_birthday()
    gender = user_input.ask_gender()
    allergies = user_input.ask_allergies()
    try:
        return Pupil(first_name, last_name, birthday, gender,
                  middle_name=middle_name, allergies=allergies)
    except ValueError as e:
        print("Could not create pupil:", e)


# READ ALL PUPILS
def display_all_pupils(school):
    if school.has_pupils():
        pupils = school.get_pupils()
        for p in pupils:
            print(p)
    else:
        print("No pupils found")


# DELETE PUPIL
def remove_pupil(school):
    if school.has_pupils():
        max_id = school.get_next_pupil_id() - 1
        pupil_id = user_input.ask_which_pupil('delete', max_id)
        p = school.find_pupil(pupil_id)
        if p is None:
            print(f"No pupil with pupil_id {pupil_id}")
            return
        print(p)
        print("You are about to delete the following pupil:")
        print(p)
        confirm = user_input.ask_confirmation("Delete")
        if confirm:
            school.delete_pupil(pupil_id)
    else:
        print("No pupils found")

# SORT PUPIL
def display_sorted_pupils(school):
    if school.has_pupils():
        sorted_list = school.get_sorted_pupils()
        for p in sorted_list:
            print(p)
    else:
        print("No pupils found")
