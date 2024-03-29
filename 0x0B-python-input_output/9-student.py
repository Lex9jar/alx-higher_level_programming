#!/usr/bin/python3
"""Defines a class 'Student'."""


class Student:
    """A Student class."""
    def __init__(self, first_name, last_name, age):
        """Initializes an instance of Student.

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dictionary representation of a 'Student' instance."""
        return self.__dict__
