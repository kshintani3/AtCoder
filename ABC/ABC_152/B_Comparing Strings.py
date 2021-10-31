A, B = map(int, input().split())
s1 = str(A) * B
s2 = str(B) * A
print(min(s1, s2))
