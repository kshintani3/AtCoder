N, M = map(int, input().split())
ans_list = [i for i in range(1000) if len(str(i)) == N]

for i in range(M):
    S, C = map(int, input().split())
    ans_list = [j for j in ans_list if str(j)[S - 1] == str(C)]

if len(ans_list) == 0:
    print(-1)
else:
    print(min(ans_list))
