#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i != j and i < j and i < 8:
            print("{}{}, ".format(i,j), end="")
        elif i != j and i < j and j == 9:
            print("{}{}".format(i,j))
