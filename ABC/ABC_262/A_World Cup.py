y = int(input())
mod = (y - 2) % 4
if mod == 0:
    print(y)
else:
    print(y + 4 - mod)
