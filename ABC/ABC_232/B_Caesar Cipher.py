s1 = input()
s2 = input()

ans = (ord(s2[-1]) - ord(s1[-1])) % 26
for i in range(len(s1) - 1):
    if ans != ((ord(s2[i]) - ord(s1[i])) % 26):
        print("No")
        exit()
print("Yes")
