N, M = map(int, input().split())
ac_list = [False] * N
wa_list = [0] * N
for _ in range(M):
    p, s = input().split()
    pp = int(p) - 1
    if not ac_list[pp] and s == "WA":
        wa_list[pp] += 1
    elif s == "AC":
        ac_list[pp] = True
wa_sum = 0
for i in range(N):
    if ac_list[i]:
        wa_sum += wa_list[i]
print(sum(ac_list), wa_sum)
