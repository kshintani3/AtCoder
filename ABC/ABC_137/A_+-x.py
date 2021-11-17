A, B = map(float, input().split())
ans = [A + B, A - B, A * B]
print(int(sorted(ans)[-1]))
