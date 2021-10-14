N, K = map(int, input().split())
ans = [1] * (N + 1)
ans[0] = 0
for _ in range(K):
    d = input()
    if d == 1:
        a = int(input())
        ans[a] = 0
    else:
        a = list(map(int, input().split()))
        for i in a:
            ans[i] = 0
print(sum(ans))
