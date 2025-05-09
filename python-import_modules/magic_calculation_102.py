#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


if __name__ == "__main__":
    # regular
    # from magic_calculator import magic_calculation

    # attempt
    import importlib.util
    import sys
    module_name = "102-magic_calculation.py"
    file_path = "102-magic_calculation.py"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    magic_calculation = getattr(module, "magic_calculation")
    # regular
    import dis
    dis.dis(magic_calculation)
