N = int(input())
S = input()
ans = ""
for i in S:
    ind = ord(i) + N
    if ind > 90:
        ind -= 26
    ans += chr(ind)
print(ans)
