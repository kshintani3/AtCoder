S = input()
S_len = len(S)
l_li, r_li = [], []
for i in range(S_len):
    if i % 2 == 0:
        l_li.append(S[i])
    else:
        r_li.append(S[i])
l_0 = l_li.count("0")
l_1 = len(l_li) - l_0
r_0 = r_li.count("0")
r_1 = len(r_li) - r_0
print(min(l_0 + r_1, l_1 + r_0))
