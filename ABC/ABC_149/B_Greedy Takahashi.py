A, B, K = map(int, input().split())
print(max(0, A - K), min(B, max(0, A + B - K)))
