t = int(input())
ff = lambda x: x * x + 2 * x + 3
print(ff(ff(ff(t) + t) + ff(ff(t))))
