N = int(input())
l = list(map(int, input().split()))
l_sum = sum(l)
for i in l:
    if 2 * i >= l_sum:
        print("No")
        exit()
print("Yes")
