S = input()
ans_list = []

for i in range(len(S)):
    ans_list.append(S[i:] + S[:i])
print(min(ans_list))
print(max(ans_list))
