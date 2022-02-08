#!/usr/bin/python3
"""
Fix My Code Module
The only thing missing was
declare first getter method
then setter method
"""


class User():
    """
    User class with getter
    and setter methods
    """

    def __init__(self):
        """ Constructor method """
        self.__email = None

    @property
    def email(self):
        """ Return email """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setting new email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
