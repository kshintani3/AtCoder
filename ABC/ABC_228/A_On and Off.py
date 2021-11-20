s, t, x = map(int, input().split())
if s > t:
    print("No" if (t <= x < s) else "Yes")
else:
    print("Yes" if (s <= x < t) else "No")

