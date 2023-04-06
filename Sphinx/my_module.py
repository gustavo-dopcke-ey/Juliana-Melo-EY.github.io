"""
Exemplo Auto-Documentação
=========================

This module contains a set of utility functions and classes.

"""

def calculate_sum(a, b):
    """
    This function calculates the sum of two numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :return: The sum of the two numbers.
    :rtype: int

    :example:

    >>> calculate_sum(2, 3)
    5
    >>> calculate_sum(0, 0)
    0
    >>> calculate_sum(-1, 1)
    0
    """
    return a + b


class MyClass:
    """
    A simple class that stores a name and age.

    :param name: The name of the person.
    :type name: str
    :param age: The age of the person.
    :type age: int
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        """
        This method prints a greeting message.

        :return: None
        """
        print("Hello, my name is {} and I'm {} years old.".format(self.name, self.age))
