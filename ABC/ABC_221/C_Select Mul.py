import itertools

N = input()
N = [int(i) for i in N]

N = sorted(N, reverse=True)
ans = 0
kai = 0
for i in range(1, len(N) // 2 + 1):
    for j in itertools.permutations(N, i):
        M_list = N[:]
        O_list = []
        for m in j:
            M_list.remove(m)
            O_list.append(m)
        M_list = map(str, M_list)
        O_list = map(str, O_list)

        # 上でsortされているのでM_listもO_listも考えられる最大となっている。
        kai = int("".join(M_list)) * int("".join(O_list))

        ans = max(ans, kai)
print(ans)
