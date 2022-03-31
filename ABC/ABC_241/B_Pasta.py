_ = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for bi in b:
    if bi in a:
        a.remove(bi)
    else:
        print("No")
        exit()
print("Yes")
