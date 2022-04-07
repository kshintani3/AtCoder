S = input()
s_li = []

for i in range(len(S)):
    s_li.append(S[i])
s_li.sort()

for j in s_li:
    print(j, end="")
