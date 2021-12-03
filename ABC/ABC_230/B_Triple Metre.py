s = input()
s_li = ["o", "x", "x"]

if s[0] == "x":
    if len(s) >= 2 and s[1] == "x":
        s = "o" + s
    else:
        s = "ox" + s

for i in range(len(s)):
    if s[i] != s_li[i % 3]:
        print("No")
        exit()
print("Yes")
