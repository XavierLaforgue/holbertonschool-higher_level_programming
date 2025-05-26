#!/usr/bin/python3
"""
Module Name: 102-square.

Defines the Square class, which represents a square with a given size.
"""


class Square:
    """
    Represents a square with a size.

    Attributes:
        size (int): The size of the square (length of a side).
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int, optional): The size of the square as a
                non-negative integer. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
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

    def __eq__(self, other) -> bool:
        """
        Check if two squares have equal area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        """
        Check if two squares have different areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other) -> bool:
        """
        Check if this square's area is greater than another's.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other) -> bool:
        """
        Check if this square's area is greater than or equal to another's.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other) -> bool:
        """
        Check if this square's area is less than another's.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other) -> bool:
        """
        Check if this square's area is less than or equal to another's.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this area is less or equal, False otherwise.
        """
        return self.area() <= other.area()


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
