import math

a, b, c = map(int, input().split())

if c == 0:
    print("=")

elif c % 2 == 0:
    if abs(a) < abs(b):
        print("<")
    elif abs(a) > abs(b):
        print(">")
    else:
        print("=")

else:
    if a * b < 0:
        if a > 0:
            print(">")
        else:
            print("<")
    else:
        if a > 0:
            if b == 0:
                print(">")
            else:
                if a < b:
                    print("<")
                elif a > b:
                    print(">")
                else:
                    print("=")
        elif a == 0:
            if 0 < b:
                print("<")
            elif 0 > b:
                print(">")
            else:
                print("=")
        else:
            if b == 0:
                print("<")
            else:
                if a < b:
                    print(">")
                elif a > b:
                    print("<")
                else:
                    print("=")
