#!/usr/bin/python3
"""
Module Name: 100-singly_linked_list.

This module contains two classes for creating and managing a
singly-linked list: Node and SinglyLinkedList.
"""


class Node:
    """
    Represent a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node | None): Reference to the next node in the
            list.
    """

    def __init__(self, data: int, next_node: "Node | None" = None):
        """
        Initialize a Node object.

        Args:
            data (int): The data value for the node.
            next_node (Node | None, optional): Reference to the next
                node. Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object nor is None.

        Examples:
            >>> my_node = Node(0)
            >>> my_node.data
            0
            >>> my_node.next_node
            >>> Node("0")
            Traceback (most recent call last):
            TypeError: data must be an integer
            >>> my_node2 = Node(0, Node(1))
            >>> my_node2.data
            0
            >>> my_node2.next_node.data
            1
            >>> Node(0, "node")
            Traceback (most recent call last):
            TypeError: next_node must be a Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self) -> int:
        """
        Get the data stored in the node.

        Returns:
            int: The data value.
        """
        return self.__data

    @data.setter
    def data(self, value: int):
        """
        Set the data for the node.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self) -> "Node | None":
        """
        Get the reference to the next node.

        Returns:
            Node | None: The next node in the list or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value: "Node | None"):
        """
        Set the reference to the next node.

        Args:
            value (Node | None): The next node in the list.

        Raises:
            TypeError: If value is not a Node object nor is None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    Represent a singly linked list.

    Attributes:
        __head (Node | None): The head node of the list.
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self) -> str:
        """
        Return a string representation of the singly linked list.

        Returns:
            str: String representation of the list.

        Examples:
            >>> sll = SinglyLinkedList()
            >>> print(sll)
            <BLANKLINE>
            >>> sll.sorted_insert(0)
            >>> print(sll)
            0
            >>> sll.sorted_insert(-1)
            >>> print(sll)
            -1
            0
            >>> sll.sorted_insert(1)
            >>> print(sll)
            -1
            0
            1
            >>> sll.sorted_insert("value")
            Traceback (most recent call last):
            TypeError: data must be an integer
        """
        node = self.__head
        sll_str = ""
        while node is not None:
            if node is not self.__head:
                sll_str += '\n'
            sll_str += str(node.data)
            node = node.next_node
        return sll_str

    def sorted_insert(self, value: int):
        """
        Insert value at the correct position of a sorted SLL.

        Inserts a new Node at the correct position into a singly linked
        list sorted in ascending order.

        Args:
            value (int): The integer value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            next_node = current_node.next_node
            while next_node is not None and value > next_node.data:
                current_node = next_node
                next_node = current_node.next_node
            current_node.next_node = new_node
            new_node.next_node = next_node


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
