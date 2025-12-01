#!/usr/bin/python3
"""
Module Name: 101-square.

Defines the Square class, which represents a square with a given size
and position.
"""


class Square:
    """
    Represents a square with a size and position.

    Attributes:
        size (int): The size of the square (length of a side).
        position (tuple): The position of the square as a tuple of two
            non-negative integers.
    """

    def __init__(self, size: int = 0,
                 position: tuple[int, int] = (0, 0)) -> None:
        """
        Initialize a Square instance.

        Args:
            size (int, optional): The size of the square as a
                non-negative integer. Defaults to 0.
            position (tuple, optional): The position as a tuple of two
                non-negative integers. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self) -> int:
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value) -> None:
        """
        Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self) -> tuple[int, int]:
        """
        Get the position of the square.

        Returns:
            tuple: The position as a tuple of two non-negative
                integers.
        """
        return self.__position

    @position.setter
    def position(self, position) -> None:
        """
        Set the position of the square.

        Args:
            position (tuple): The new position as a tuple of two
                non-negative integers.

        Raises:
            TypeError: If position is not a tuple of two non-negative
            integers.
        """
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(elem, int) for elem in position) or
                any(map(lambda x: x < 0, position))):
            raise TypeError('position must be a tuple of 2 positive '
                            'integers')
        self.__position = position

    def area(self) -> int:
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self) -> None:
        """Print the square at position using the '#' character."""
        if not self.__size:
            print()
            return
        print("\n"*self.__position[1], end="")
        for _ in range(self.__size):
            print(" "*self.__position[0], end="")
            print("#"*self.__size)

    def __str__(self) -> str:
        """
        Return a string representation of the square.

        The square is drawn using the '#' character. The string
        includes leading newlines and spaces based on the square's
        position. If the size is 0, returns an empty string.

        Returns:
            str: The formatted square as a string.
        """
        if not self.__size:
            return ""
        square_str = ("\n" * self.__position[1]
                      + "\n".join([" " * self.__position[0]
                                   + '#' * self.__size] * self.__size))
        return square_str


if __name__ == "__main__":
    """
    Runs doctests, pycodestyle, and pydocstyle checks on the module.

    This block is used for testing and linting the module using
    doctest, pycodestyle, and pydocstyle tools.
    """

    # reminder:
    # flake8 -> linter (like picodestyle)
    # mypy -> checks if the code has mistakes
    # pre_commit -> forbids commits in case of not compliance of selected
    # tests (flake8, doctest, mypy)

    from os.path import basename, exists
    from doctest import testmod, testfile
    from pycodestyle import StyleGuide
    from pydocstyle import check

    def check_mod_name_docstring(file_name: str) -> None:
        """
        Check module docstring for module name.

        Checks if the module docstring starts with the formula 'Module
        Name: <filename>'.
        """
        actual_doc = __doc__
        if actual_doc is None:
            print("❌ Missing module docstring❌")
            return
        actual_doc_first_line = actual_doc.splitlines()[1]
        expected_mod_doc_prefix = "Module Name: "
        actual_mod_doc_prefix = actual_doc_first_line[:13].lstrip()
        if actual_mod_doc_prefix != expected_mod_doc_prefix:
            print(f"❌ Module docstring doesn't start with the usual "
                  f"prefix: {expected_mod_doc_prefix}❌")
            return
        mod_name = file_name.replace('.py', '')
        expected_doc_mod_name = f"{mod_name}"
        actual_doc_mod_name = actual_doc_first_line.split()[2][:-1]
        if actual_doc_mod_name == expected_doc_mod_name:
            print("✅ Module docstring module name is correct✅")
        else:
            expected_first_line = (expected_mod_doc_prefix
                                   + expected_doc_mod_name + '.')
            print(f"❌ Incorrect module name in module docstring❌\n"
                  f"\t{'Found:':9s} '{actual_doc_first_line}'\n"
                  f"\t{'Expected:':9s} '{expected_first_line}'")

    def run_doctests(file_name: str,
                     test_file_path: str = "") -> None:
        """
        Run doctests on module and (optional) external test file.

        Args:
            file_path (str): Path to the module file. test_file_path
            (str): Path to the external doctest file.
        """
        if (not isinstance(file_name, str) or
                not isinstance(test_file_path, str)):
            raise TypeError('file_name and test_file_path must be '
                            'strings')
        total_failed = 0
        total_tests = 0
        # Run doctests from external test file.
        if test_file_path.strip() and exists(test_file_path):
            print(f"🔍 Running doctests on {test_file_path}🔍")
            file_result = testfile(test_file_path, verbose=False)
            total_failed += file_result.failed
            total_tests += file_result.attempted
        elif test_file_path.strip():
            print(f"⚠️  Test file {test_file_path} not found. "
                  "Skipping external file doctests⚠️")
        print(f"🔍 Running doctests on {file_name}🔍")
        # Run module-level doctests. name is the file with the module.
        mod_result = testmod(name=file_name, verbose=False)
        # doctest.testmod and doctest.testfile return testResults
        # objects with attributes: failed and attempted.
        total_failed += mod_result.failed
        total_tests += mod_result.attempted
        if total_failed == 0:
            print(f"✅ All {total_tests} doctests passed✅")
        else:
            print(f"❌ {total_failed} of {total_tests} doctests "
                  "failed❌")

    def run_pycodestyle(file_name):
        """
        Run pycodestyle on the given filename.

        Args:
            file_path (str): Path to the file to check.
        """
        print(f"{'*'*72}\n🔍 Running pycodestyle on {file_name}🔍")
        result = StyleGuide().check_files([file_name])
        if result.total_errors == 0:
            print("✅ pycodestyle passed.✅")
        else:
            print(f"❌ pycodestyle found {result.total_errors} "
                  "issues.❌")

    def run_pydocstyle(file_name):
        """
        Run pydocstyle on the given filename.

        Args:
            file_path (str): Path to the file to check.
        """
        print(f"{'*'*72}\n🔍 Running pydocstyle on {file_name}🔍")
        report = check([file_name])
        error_count = 0
        for error in report:
            print(f"{error}")
            error_count += 1
        if error_count == 0:
            print("✅ pydocstyle passed.✅")
        else:
            print(f"❌ pydocstyle found {error_count} issues.❌")
    file_name = basename(__file__)
    check_mod_name_docstring(file_name)
    test_file_path = ""
    run_doctests(file_name, test_file_path)
    run_pycodestyle(file_name)
    run_pydocstyle(file_name)
