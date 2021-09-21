A, B = map(str, input().split())

a = map(int, A)
b = map(int, B)

print(max(sum(a), sum(b)))
