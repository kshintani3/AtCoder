N = int(input())
tree_list = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree_list[a - 1].append(b - 1)
    tree_list[b - 1].append(a - 1)
for i in tree_list:
    if len(i) == N - 1:
        print("Yes")
        exit()
print("No")
