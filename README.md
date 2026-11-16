# Sun Valley School Register

A Python console application for a school secretary to register and manage pupils.
Exam project for the Programming course at EK, autumn 2026.

## How to run

Requires Python 3.10 or newer (the menus use `match`-case). No external packages are needed.

    python main.py

To run the tests:

    python test_school.py

## Features

**Implemented (pupils):**
- Register a new pupil. A unique `pupil_id` is assigned automatically.
- List all pupils
- Update a pupil's personal details, one field at a time
- Delete a pupil, with confirmation
- Sort pupils by last name

**Planned, not yet implemented:**
- Find a pupil by name
- Classroom management (create, list, update, delete, sort)
- Place a pupil in a classroom, with a capacity check
- Show pupils in a classroom, and pupils without a classroom
- Save to and load from file

## Project structure

| File | Purpose |
|---|---|
| `main.py` | Entry point. Main menu loop |
| `submenus.py` | Pupil and classroom menus; display and user dialogue |
| `user_input.py` | Prompts that collect and convert user input |
| `school.py` | `School` class. Holds the lists of pupils and classrooms |
| `pupil.py` | `Pupil` class |
| `classroom.py` | `Classroom` class |
| `validators.py` | Validation rules for single values (names, dates, numbers, class ids) |
| `enums.py` | `Gender` and `Letter` enumerations |
| `test_school.py` | Tests with good and bad cases |
| `docs/` | Original class and flow diagrams from the design phase, and the exam proposal |

## Design

- **Separation of concerns:** the model (`School`, `Pupil`, `Classroom`) stores and validates data
  and never talks to the user. The menus and input functions handle all user interaction.
- **Encapsulation:** attributes are private and only reachable through getters and setters.
  Setters call the validators, so an object can never hold an invalid value.
- **Composition:** `School` holds the lists of `Pupil` and `Classroom` objects and is responsible
  for adding, finding, updating and deleting them.
- **Database-style references:** pupils and classrooms are linked by id (`pupil_id`, `class_id`),
  analogous to primary and foreign keys, so pupils can be unassigned or move between classrooms.

## Author

Helen Connor Sørensen
