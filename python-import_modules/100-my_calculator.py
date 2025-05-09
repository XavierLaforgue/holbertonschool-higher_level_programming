#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    if sys.argv[2] not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = ".format(a, sys.argv[2], b), end="")
    if sys.argv[2] == "+":
        print(add(a, b))
    if sys.argv[2] == "-":
        print(sub(a, b))
    if sys.argv[2] == "*":
        print(mul(a, b))
    if sys.argv[2] == "/":
        print(div(a, b))
