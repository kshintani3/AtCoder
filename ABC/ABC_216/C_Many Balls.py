N = int(input())
binN = bin(N)
str_binN = str(binN)
list_str_bin_N = list(str_binN)
list_bin_N = list_str_bin_N[2:]
# print(list_bin_N)

ans = []
for i, b in enumerate(list_bin_N):
    if b == "1":
        ans.append("A")
        if i != len(list_bin_N) - 1:
            ans.append("B")
    else:
        if i != len(list_bin_N) - 1:
            ans.append("B")
ans_str = ""
for a in ans:
    ans_str += a

print(ans_str)
