A, B, K = map(int, input().split())
cn = 0
while A < B:
    A *= K
    cn += 1
print(cn)
