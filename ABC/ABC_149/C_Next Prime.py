X = int(input())
while True:
    x_list = [i for i in range(2, int(X ** 0.5) + 1) if X % i == 0]
    if len(x_list) == 0:
        print(X)
        exit()
    X += 1
