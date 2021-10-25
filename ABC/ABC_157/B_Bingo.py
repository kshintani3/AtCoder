a = [list(map(int, input().split())) for i in range(3)]
a = a[0] + a[1] + a[2]
a_list = [False] * 9
N = int(input())
ans = False
for _ in range(N):
    b = int(input())
    if b in a:
        a_list[a.index(b)] = True
for i in range(3):
    if a_list[i * 3] and a_list[i * 3 + 1] and a_list[i * 3 + 2]:
        ans = True
    elif a_list[i] and a_list[i + 3] and a_list[i + 6]:
        ans = True
if a_list[0] and a_list[4] and a_list[8]:
    ans = True
elif a_list[2] and a_list[4] and a_list[6]:
    ans = True
print("Yes" if ans else "No")
