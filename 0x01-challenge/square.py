#!/usr/bin/python3
"""
Fix My Code Module
The only thing missing was
the multiplication of the height
by the width in the Area method.
"""


class Square():
    """
    Square Class with methods to get
    Perimeter and Area
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Constructor Method"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Get perimeter of square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Print Square like this: width/height """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
