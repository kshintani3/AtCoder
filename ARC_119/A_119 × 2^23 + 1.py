n = int(input())
min = n

for b in range(60):
    a = n // (2 ** b)
    c = n % (2 ** b)
    if a + b + c < min:
        min = a + b + c

print(min)
