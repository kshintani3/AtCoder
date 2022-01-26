s = input()
A, B = map(int, input().split())
print(s[:A - 1] + s[B - 1] + s[A:B - 1] + s[A - 1] + s[B:])
