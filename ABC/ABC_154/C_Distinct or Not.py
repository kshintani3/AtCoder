N = int(input())
a = list(map(int, input().split()))
a_set = list(set(a))

print("YES" if N == len(a_set) else "NO")
