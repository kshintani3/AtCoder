a, b, c = map(int, input().split())
a **= c % 6
b **= c % 6
print('=<>'[(a < b) - (a > b)])
