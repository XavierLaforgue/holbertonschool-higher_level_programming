#!/usr/bin/python3
r"""
Module name: "4-rectangle.py".

Description:

    Contains a class Rectangle that defines a rectangle by its width
    and height and offers methods to obtain its area and perimeter.
    __str__ and __repr__ magic methods are also defined.

Classes:
    Rectangle: defines a rectangle by its width and height, makes area
        and perimeter methods available.
        Casting to string (creating a new string object for it) is
        possible, it returns a string made up of the characters '#'
        (for each unit length) and '\n' (to separate the rows) as
        necessary.  Thus, making print() draw a rectangle made of #.
        The canonical string representation is provided such that eval
        may recreate the Rectangle instance.
"""


class Rectangle(object):
    r"""
    Creates a class Rectangle.

    Description:
        The created Rectangle object is defined by private instance
        attributes width and height, and methods area and perimeter.
        The casting method (__str__) is also made available to create a
        string to represent the rectangle with the character '#' as its
        unit element and '\n' to delimit the rows of characters that
        will make up a drawing of the rectangle if print is used. The
        canonical string representation method (__repr__) is also made
        available such that eval may recreate the Rectangle instance.

    Examples:
        >>> Rectangle(3, 2)
        Rectangle(3, 2)
        >>> type(Rectangle()) # doctest: +ELLIPSIS
        <class '__main__.Rectangle'>
    """

    def __init__(self, width: int = 0, height: int = 0):
        """
        Initialize Rectangle object.

        Description:
            The created instance takes two optional arguments, each
            which may be set to the corresponding private attribute via
            its property setter.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Getter for the width private instance attribute."""
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
        """Getter for the height private instance attribute."""
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
        """
        User-friendly string representation of the instance.

        Description:
            Sets up the behavior when the functions str and/or print
            are applied on a Rectangle instance.
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
        """
        return f"Rectangle({self.width}, {self.height})"

    def area(self) -> int:
        """Calculate and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> int:
        """Calculate and returns the perimeter of the rectangle."""
        if not self.width or not self.height:
            return 0
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    import doctest
    import pycodestyle

    def run_doctests(file_path):
        """Run doctest from current module file and from test file."""
        print(f"🔍 Running doctests on {file_path}...")

        # Run module-level doctests
        mod_result = doctest.testmod(verbose=False)

        # Run doctests from external file
        file_result = doctest.testfile(file_path, verbose=False)

        total_failed = mod_result.failed + file_result.failed
        total_tests = mod_result.attempted + file_result.attempted

        if total_failed == 0:
            print(f"✅ All {total_tests} doctests passed.")
        else:
            print(f"❌ {total_failed} of {total_tests} doctests "
                  "failed.")

    def run_pycodestyle(file_path):
        """Run pycodestyle on the given filename."""
        print(f"🔍 Running pycodestyle on {file_path}...")
        style = pycodestyle.StyleGuide()
        result = style.check_files([file_path])
        if result.total_errors == 0:
            print("✅ pycodestyle passed.")
        else:
            print(f"❌ pycodestyle found {result.total_errors} "
                  "issues.")

    from pydocstyle import check

    def run_pydocstyle(file_path):
        """Run pydocstyle on the given filename."""
        print(f"🔍 Running pydocstyle on {file_path}...")
        report = check([file_path])
        error_count = 0
        for error in report:
            print(f"{error}")
            error_count += 1
        if error_count == 0:
            print("✅ pydocstyle passed.")
        else:
            print(f"❌ pydocstyle found {error_count} issues.")

    file = "4-rectangle.py"
    test_file_path = "tests/test_rectangle_4.txt"
    run_doctests(test_file_path)
    run_pycodestyle(file)
    run_pydocstyle(file)
