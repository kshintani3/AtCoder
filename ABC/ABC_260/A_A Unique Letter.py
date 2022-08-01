s = [c for c in input()]
for i in s:
    if s.count(i) == 1:
        print(i)
        exit()
print(-1)