H, W = map(int, input().split())
a = []
ans = []

for _ in range(H):
    ai = input()
    if "#" in ai:
        a.append(ai)

for j in zip(*a):
    if "#" in j:
        ans.append(j)

for i in zip(*ans):
    print("".join(i))
