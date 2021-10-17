S = input()
ans_list = [S]
S_list = []
for i in S:
    S_list.append(i)
for _ in range(len(S)):
    ans = ""
    ss = S_list.pop(0)
    S_list.append(ss)
    for i in S_list:
        ans += i
    ans_list.append(ans)
ans_list.sort()
print(ans_list[0])
print(ans_list[-1])
