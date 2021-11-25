N = int(input())
w = list(map(int, input().split()))
w_s = sum(w)
print(min([abs(w_s - 2 * sum(w[:i])) for i in range(1, N)]))
