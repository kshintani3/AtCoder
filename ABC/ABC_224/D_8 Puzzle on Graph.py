M = int(input())
adj = [[] for _ in range(9)]
p_con = [i for i in range(9)]

for i in range(M):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    adj[s].append(t)
    adj[t].append(s)
p = list(map(int, input().split()))
p = [i - 1 for i in p]
p_s = []

# 揃っていないパズルのindex
for i in range(8):
    if i != p[i]:
        p_s.append(i)

if len(p_s) == 0:
    print(0)
    exit()

kuu = list(set(p_con) ^ set(p))[0]
