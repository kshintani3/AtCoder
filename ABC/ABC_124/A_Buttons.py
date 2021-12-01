A, B = map(int, input().split())
ans = max(A, B) * 2
print(ans if A == B else ans - 1)
