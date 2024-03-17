#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    num_arguments = len(sys.argv)
    expected_args = 4
    if num_arguments != expected_args:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if sys.argv[2] not in {"+", "-", "*", "/"}:
            print("Unknown operator. Available operators: +, -, and /")
            sys.exit(1)
        else:
            operator = sys.argv[2]

            if operator == "+":
                result = add(a, b)
            elif operator == "-":
                result = sub(a, b)
            elif operator == "*":
                result = mul(a, b)
            elif operator == "/":
                result = div(a, b)

            print("{} {} {}  = {}".format(a, operator, b, result))
