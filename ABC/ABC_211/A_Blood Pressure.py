a, b = map(int, input().split())

c = (a-b)/3 + b

if c % 1 == 0:
    print(int(c))
else:
    print(c)