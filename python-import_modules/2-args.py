#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_args = len(sys.argv) - 1
    arg_label = "argument" if n_args == 1 else "arguments"
    args_punct = ":" if n_args > 0 else "."
    print("{} {}{}".format(n_args, arg_label, args_punct))
    for i in range(1, n_args + 1):
        print(f"{i}: {sys.argv[i]}")
