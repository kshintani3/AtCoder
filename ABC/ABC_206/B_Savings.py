N = int(input())
ans = 0
for i in range(1, 10 ** 9):
    ans += i
    if N <= ans:
        print(i)
        break
