n = int(input())
s = input()
a = [int(c) for c in s]

for i in range(n):
    if a[i] == 0:
        continue
    else:
        if i % 2 == 1:
            print("Aoki")
        else:
            print("Takahashi")
        break
