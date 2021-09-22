N, M = map(int, input().split())

if N == M:
    print(0)

elif M == 0:
    print(1)

else:
    a = list(map(int, input().split()))
    a.sort()
    a.insert(0, 0)
    a.append(N + 1)
    a_list = [a[i + 1] - a[i] - 1 for i in range(M + 1)]

    a_list = [j for j in a_list if j > 0]

    seal = min(a_list)
    ans = 0

    for i in a_list:
        ans += (i + seal - 1) // seal

    print(ans)
