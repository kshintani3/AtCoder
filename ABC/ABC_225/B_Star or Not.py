N = int(input())
tree_list = [0 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree_list[a - 1] += 1
    tree_list[b - 1] += 1

print("Yes" if tree_list[a - 1] == N - 1 or tree_list[b - 1] == N - 1 else "No")
