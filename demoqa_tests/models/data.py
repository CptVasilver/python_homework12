from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    second_name: str
    email: str
    gender: str
    phone_number: int
    day_of_birth: int
    month_of_birth: str
    year_of_birth: int
    subjects: str
    hobbies: [str]
    picture: str
    address: str
    state: str
    city: str
