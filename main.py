# Sun Valley School Register
# Helen Connor Sørensen
# Project for EK programmings exam, Autumn 2026

from datetime import date
from enums import Gender
from pupil import Pupil
from classroom import Classroom
from school import School

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


def main():
    school = School()
    running=True
    while running == True:
        print("")
        print("Welcome to Sun Valley's registration system.")
        print("What would you like to work?")
        print("1. Pupils")
        print("2. Classes")
        print("0. Exit and save")
        choice = input("Which choice would you like to make?  ")

        match choice:
            case "1": pupil_menu(school)
            case "2": classroom_menu(school)
            case "0":
                print("Exiting...")
                running = False
            case _:
                print("Invalid choice")



if __name__ == "__main__": # this checks that running file is main.py
    main()
