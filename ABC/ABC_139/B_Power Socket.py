A, B = map(int, input().split())
A_sum = 1
for i in range(0, 100):
    if A_sum >= B:
        print(i)
        exit()
    A_sum += A - 1
