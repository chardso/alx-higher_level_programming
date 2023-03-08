#!/usr/bin/python3

for a in range(0, 8):
    for k in range(a + 1, 10):
        print("{:d}{:d}".format(a, k), end=', ')
print("{:d}{:d}".format(a + 1, k))

