from collections import Counter

s = input()
ans = not s.islower() and not s.isupper() and len(Counter(s).keys()) == len(s)

print("Yes" if ans else "No")
