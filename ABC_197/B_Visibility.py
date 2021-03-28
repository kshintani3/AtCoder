ra = list(map(int, input().split()))
s = [list(input()) for i in range(ra[0])]

h = ra[0] - 1
w = ra[1] - 1
x = ra[2] - 1
y = ra[3] - 1

count = 1

for i in range(y): #(x,y)から左方向,w-y=2
    if s[x][y-i-1] == '.':
        count += 1
    else:
        break

for i in range(w-y): #(x,y)から右方向
    if s[x][y+i+1] == '.':
        count += 1
    else:
        break

for i in range(x): #(x,y)から上方向
    if s[x-i-1][y] == '.':
        count += 1
    else:
        break

for i in range(h-x): #(x,y)から下方向
    if s[x+i+1][y] == '.':
        count += 1
    else:
        break

print(count)
