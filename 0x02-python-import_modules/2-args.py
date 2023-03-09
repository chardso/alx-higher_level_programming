#!/usr/bin/python3

def args():
    import sys

    sys.argv.pop(0)
    if len(sys.argv) != 1:
        print("{} arguments:".format(len(sys.argv)))
    else:
        print("{} argument:".format(len(sys.argv)))
    for i in range(len(sys.argv)):
        print("{0}: {1}".format(i + 1, sys.argv[i]))


if __name__ == "__main__":
    args()

