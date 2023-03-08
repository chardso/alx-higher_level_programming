#!/usr/bin/python3

for a in range(97, 123):
    if chr(a) != 'q' and chr(a) != 'e':
        print("{i}".format(a=chr(a)), sep="", end="")

