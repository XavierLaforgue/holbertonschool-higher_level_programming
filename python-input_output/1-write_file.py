#!/usr/bin/python3
"""
Module Name: 1-write_file.

Contains function that writes to a file.
"""


def write_file(filename="", text=""):
    """Write text to a file.

    Args:
        filename (str): name of the file to write the text on.
        text (str): text to write into the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        written_text = f.write(text)
    return written_text


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
