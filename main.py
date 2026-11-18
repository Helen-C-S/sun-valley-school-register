# Sun Valley School Register
# Helen Connor Sørensen
# Project for EK programmings exam, Autumn 2026

from school import School
import submenus

def main():
    school = School()
    running=True
    while running == True:
        print("")
        print("Welcome to Sun Valley School's registration system.")
        print("What would you like to work with?")
        print("1. Pupils")
        print("2. Classes (limited functionality)")
        print("0. Save and exit")
        choice = input("Which choice would you like to make?  ")

        match choice:
            case "1": submenus.pupil_menu(school)
            case "2": submenus.classroom_menu(school)
            case "0":
                school.save_pupils()
                print("Exiting...")
                running = False
            case _:
                print("Invalid choice")



if __name__ == "__main__": # this checks that running file is main.py
    main()
