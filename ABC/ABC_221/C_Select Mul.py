import itertools

N = input()
N_list = [int(i) for i in N]

N_list = sorted(N_list, reverse=True)
ans = 0
kai = 0
for i in range(1, len(N_list) // 2 + 1):
    for j in itertools.permutations(N_list, i):
        M_list = N_list[:]
        O_list = []
        for m in j:
            M_list.remove(m)
            O_list.append(m)
        M_list = map(str, M_list)
        O_list = map(str, O_list)
        kai = int("".join(M_list)) * int("".join(O_list))
        if ans < kai:
            ans = kai
print(ans)
