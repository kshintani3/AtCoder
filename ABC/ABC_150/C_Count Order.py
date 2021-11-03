import itertools

N = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
p_str, q_str = "", ""
for j in p:
    p_str += str(j)
for j in q:
    q_str += str(j)

p_cnt, q_cnt = 0, 0
cnt = 0

for i in itertools.permutations(range(1, N + 1)):
    i_str = ""
    cnt += 1
    for j in i:
        i_str += str(j)
    if i_str == p_str:
        p_cnt = cnt
    if i_str == q_str:
        q_cnt = cnt
print(abs(q_cnt - p_cnt))
