N = int(input())
ans_min = 10 ** 12

for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        if ans_min > N // i + i - 2:
            ans_min = N // i + i - 2
print(ans_min)
