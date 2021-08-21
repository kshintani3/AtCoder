import itertools

S, K = map(str, input().split())
K = int(K)
S_list = sorted(list(S))

comb_list = list(set(itertools.permutations(S_list)))

ans_list = []

for i in comb_list:
    ans_list.append("".join(i))

ans_list.sort()

print(ans_list[K - 1])
