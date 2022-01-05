N = int(input())
li = []
for _ in range(N):
    li.append(input())
if len(set(li)) == N:
    for i in range(N - 1):
        if li[i][-1] != li[i + 1][0]:
            print("No")
            exit()
    print("Yes")
else:
    print("No")
