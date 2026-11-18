# Place to keep variable validation when creating objects or loading objects
# Helen Connor Sørensen
# 13.11.2026

from datetime import date
from enums import Gender
MAX_NAME_LENGTH = 50
MIN_NAME_LENGTH = 2
MIN_BIRTH_YEAR = 2000


def validate_name(value, label):
    if value is None or not value.strip():
        raise ValueError(f"{label} cannot be empty")
    for ch in value:
        if ch.isdigit():
            raise ValueError(f"{label} cannot contain numbers")
    value = value.strip()
    if ";" in value:
        raise ValueError(f"{label} cannot contain a semicolon")
    if len(value) > MAX_NAME_LENGTH:
        raise ValueError(f"{label} cannot be longer than {MAX_NAME_LENGTH} characters")
    if len(value) < MIN_NAME_LENGTH:
        raise ValueError(f"{label} cannot be shorter than {MIN_NAME_LENGTH} characters")
    return value

def validate_optional_text(value, label, allow_digits=True):
    if value is None or not value.strip():
        value = None
    elif len(value.strip()) > MAX_NAME_LENGTH:
        raise ValueError(f"{label} cannot be longer than {MAX_NAME_LENGTH} characters")
    else:
        value = value.strip().replace(";",",") # semi-colon is the seperator for saving/loading
        if not allow_digits:
            for ch in value:
                if ch.isdigit():
                    raise ValueError(f"{label} cannot contain numbers")
    return value

def validate_date(value, label):
    if isinstance(value, str):
        value = date.fromisoformat(value)  # raises ValueError on bad format
    if value >= date.today():
        raise ValueError(f"{label} cannot be in the future")
    return value

def validate_gender(value):
    if not isinstance(value, Gender):
        raise ValueError("Gender must be either Male (M), Female (F) or Non-binary (N)")
    return value

def validate_int_range(value, label, min_value, max_value=None):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{label} cannot be empty")
    try:
        value = int(value)  # 10.11.2026
    except ValueError:
        raise ValueError(f"{label} must be a whole number")
    if value < min_value:
        raise ValueError(f"{label} must be {min_value} or greater")
    if max_value is not None and value > max_value:
        raise ValueError(f"{label} cannot be greater than {max_value}")
    return value

def validate_year(year):
    try:
        if len(year) != 4:
            raise ValueError("Please enter numbers in YYYY format")
    except ValueError as e:
        print(e)
    year = validate_int_range(year, "The year", MIN_BIRTH_YEAR, date.today().year)
    return year