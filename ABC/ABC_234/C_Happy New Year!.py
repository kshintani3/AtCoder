K = int(input())
k_bin = bin(K)
ans = ""

for i in k_bin[2:]:
    if i == "1":
        ans += "2"
    else:
        ans += i
print(ans)
