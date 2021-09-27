N = int(input())

ans = []

for i in range(1, 10 ** 6 + 1):
    if N % i == 0:
        ans.append(i)
        ans.append(N // i)
    if i * i > N:
        break
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)
