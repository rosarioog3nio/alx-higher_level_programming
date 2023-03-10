#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all the args"""
    import sys

    total = 0
    for tot in range(len(sys.argv) - 1):
        total += int(sys.argv[tot + 1])
    print("{}".format(total))
