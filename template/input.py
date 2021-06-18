h = 3 #縦の数
w = 4 #横の数

#入力例
# 10 20 00
a = input().split()
a, b, c = map(int,input().split())
a = list(map(int, input().split()))
s = int(input())
print(s[4])

# 1
# 2
# 1
# 6
# 1
a = [int(input()) for i in range(5)]

# oxox
# xxxo
# xxox
s = [list(input()) for l in range(h)]

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
p = [input().split() for l in range(h)]

# 12345678
s = input()
a = [int(c) for c in s]

# 1 a
# 3 b
# 5 c
# 7 d
# 9 e
list = []
for i in range(5):
    a,b=input().split()
    list.append((int(a), b))

# 1 300 400 700
# 2 500 200 700
# 3 100 900 1000
# 4 800 400 1200
xy = [map(int, input().split()) for _ in range(h)]
a,b,c,d = [list(i) for i in zip(*xy)]