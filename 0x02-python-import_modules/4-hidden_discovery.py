#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    files = dir(hidden_4)
    for i in files:
        if i[0] != "_":
            print(i)
