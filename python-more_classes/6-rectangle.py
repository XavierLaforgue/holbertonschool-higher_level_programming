#!/usr/bin/python3
r"""
Module name: "6-rectangle.py".

Description:
    Contains a class Rectangle that defines a rectangle by its width
    and height and offers methods to obtain its area and perimeter.
    __str__, __repr__, and __del__ magic methods are also defined.
    Includes a counter of currently existing instances.

Classes:
    Rectangle: defines a rectangle by its width and height, makes area
        and perimeter methods available.
        Casting to string (creating a new string object for it) is
        possible, it returns a string made up of the characters '#'
        (for each unit length) and '\n' (to separate the rows) as
        necessary.  Thus, making print() draw a rectangle made of #.
        The canonical string representation is provided such that eval
        may create a copy of the current Rectangle instance.
        A message is printed on instance deletion.
        The number of object instances currently in existence is
        accessible via the class.
"""


class Rectangle(object):
    r"""
    Creates a class Rectangle.

    Description:
        The created Rectangle object is defined by private instance
        attributes width and height, and public methods area and
        perimeter. The class public attribute number_of_instances
        counts the Rectangles currently in existence.
        The casting method (__str__) is also made available to create a
        string to represent the rectangle with the character '#' as its
        unit element and '\n' to delimit the rows of characters that
        will make up a drawing of the rectangle if print is used. The
        canonical string representation method (__repr__) is also made
        available such that eval may recreate the Rectangle instance.
        __del__ is set such that a message is printed when an instance
        of Rectangle is deleted.
    """

    number_of_instances = 0

    def __init__(self, width: int = 0, height: int = 0):
        """
        Initialize Rectangle object.

        Description:
            The created instance takes two optional arguments, each
            which may be set to the corresponding private attribute via
            its property setter.

        Examples:
            >>> Rectangle.number_of_instances
            0
            >>> rect = Rectangle() # no arguments
            >>> Rectangle.number_of_instances
            1
            >>> type(rect)
            <class '__main__.Rectangle'>
            >>> rect.width, rect.height
            (0, 0)
            >>> rect = Rectangle(3) # only width given
            >>> Rectangle.number_of_instances
            1
            >>> rect.width, rect.height
            (3, 0)
            >>> rect = Rectangle(height=2) # only height given
            >>> Rectangle.number_of_instances
            1
            >>> rect.width, rect.height
            (0, 2)
            >>> rect = Rectangle(3, 2) # width and height given
            >>> Rectangle.number_of_instances
            1
            >>> rect.width, rect.height
            (3, 2)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self) -> int:
        """
        Getter for the width private instance attribute.

        Examples:
            >>> rect = Rectangle("-2")
            Traceback (most recent call last):
            TypeError: width must be an integer
            >>> rect = Rectangle(-2)
            Traceback (most recent call last):
            ValueError: width must be >= 0
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        """
        Setter for the width private attribute.

        Description:
            It ensures the input value for width is a positive integer
            before assigning it to the instance attribute, it raises
            errors if undesired input.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self) -> int:
        """
        Getter for the height private instance attribute.

        Examples:
            >>> rect = Rectangle(height="-3")
            Traceback (most recent call last):
            TypeError: height must be an integer
            >>> rect = Rectangle(height=-3)
            Traceback (most recent call last):
            ValueError: height must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, value: int):
        """
        Setter for the height private attribute.

        Description:
            It ensures the input value for height is a positive integer
            before assigning it to the instance attribute, it raises
            errors if undesired input.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def __str__(self) -> str:
        r"""
        User-friendly string representation of the instance.

        Description:
            Sets up the behavior when the functions str and/or print
            are applied on a Rectangle instance.

        Examples:
            >>> rect = Rectangle(2, 3)
            >>> str(rect)
            '##\n##\n##'
            >>> print(str(rect))
            ##
            ##
            ##
            >>> print(rect)
            ##
            ##
            ##
        """
        if not self.width or not self.height:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self) -> str:
        """
        Canonical string representation of the instance.

        Description:
            Sets up the canonical string representation of the instance
            such that eval may be able to recreate that instance (make
            a new instance identical to the reference).

        Examples:
            >>> rect1 = Rectangle(2, 1); print(repr(rect1))
            Rectangle(2, 1)
            >>> rect2 = eval(repr(rect1)); print(rect2)
            ##
            >>> type(rect1); type(rect2);
            <class '__main__.Rectangle'>
            <class '__main__.Rectangle'>
            >>> rect1 == rect2
            False
        """
        return f"Rectangle({self.width}, {self.height})"

    def area(self) -> int:
        """
        Calculate and returns the area of the rectangle.

        Examples:
            >>> rect = Rectangle(3, 5); rect.area()
            15
        """
        return self.width * self.height

    def perimeter(self) -> int:
        """
        Calculate and returns the perimeter of the rectangle.

        Examples:
            >>> rect = Rectangle(3, 5); rect.perimeter()
            16
        """
        if not self.width or not self.height:
            return 0
        return 2 * (self.width + self.height)

    suppress_del_print = False  # Class-level flag

    def __del__(self):
        """
        Set actions to perform on instance deletion.

        Examples:
            >>> rect = Rectangle(4, 2); print(rect)
            ####
            ####
            >>> Rectangle.suppress_del_print = False
            >>> del rect
            Bye rectangle...
            >>> Rectangle.suppress_del_print = True
        """
        Rectangle.number_of_instances -= 1
        if not self.suppress_del_print:
            print("Bye rectangle...")


if __name__ == "__main__":
    import doctest
    import pycodestyle
    from pydocstyle import check

    def run_doctests(file_path, test_file_path):
        """Run doctest from current module file and from test file."""
        print(f"🔍 Running doctests on {file_path} and "
              f"{test_file_path}🔍")

        # Suppress __del__ printing
        Rectangle.suppress_del_print = True

        # Run module-level doctests. name is the file with the module.
        mod_result = doctest.testmod(name=file_path, verbose=False)
        """ doctest.testmod returns a TestResults object with
        attributes: failed and attempted."""

        # Run doctests from external file.
        file_result = doctest.testfile(test_file_path, verbose=False)
        """ doctest.testfile also returns a TestResults object with
        attributes: failed and attempted."""

        total_failed = mod_result.failed + file_result.failed
        total_tests = mod_result.attempted + file_result.attempted

        if total_failed == 0:
            print(f"✅ All {total_tests} doctests passed.✅")
        else:
            print(f"❌ {total_failed} of {total_tests} doctests "
                  "failed.❌")
        # Suppress __del__ printing
        Rectangle.suppress_del_print = False

    def run_pycodestyle(file_path):
        """Run pycodestyle on the given filename."""
        print(f"{'*'*72}\n🔍 Running pycodestyle on {file_path}🔍")
        style = pycodestyle.StyleGuide()
        result = style.check_files([file_path])
        if result.total_errors == 0:
            print("✅ pycodestyle passed.✅")
        else:
            print(f"❌ pycodestyle found {result.total_errors} "
                  "issues.❌")

    def run_pydocstyle(file_path):
        """Run pydocstyle on the given filename."""
        print(f"{'*'*72}\n🔍 Running pydocstyle on {file_path}🔍")
        report = check([file_path])
        error_count = 0
        for error in report:
            print(f"{error}")
            error_count += 1
        if error_count == 0:
            print("✅ pydocstyle passed.✅")
        else:
            print(f"❌ pydocstyle found {error_count} issues.❌")

    file_path = "6-rectangle.py"
    test_file_path = "tests/test_rectangle_6.txt"
    run_doctests(file_path, test_file_path)
    run_pycodestyle(file_path)
    run_pydocstyle(file_path)
