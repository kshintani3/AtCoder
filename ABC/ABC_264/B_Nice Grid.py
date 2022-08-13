r, c = map(int, input().split())
m = min([r, 16-r, c, 16 - c])
print('black' if m % 2 == 1 else 'white')
