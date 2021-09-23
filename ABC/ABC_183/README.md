# AtCoder Beginner Contest 183
## C - Travel
- `itertools.permutations(a)` : リスト`a`に含まれる要素の順列
```python:
import itertools

a = range(3)
b = itertools.permutations(a)
for i in b:
    print(i)

# 出力結果
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)
```
(補足) - `itertools.combinations(a, r)` : リスト`a`に含まれる要素から`r`個選ぶ組み合わせ(順序を無視)
```python:
import itertools

a = list(range(4))
b = itertools.combinations(a, 3)
for i in b:
    print(i)

# 出力結果
(0, 1, 2)
(0, 1, 3)
(0, 2, 3)
(1, 2, 3)
```

## D - Water Heater
- `itertools.accumulate(a)` : リスト`a`の累積和。第2引数を指定することで累積積なども算出可能
```python:
import itertools
import operator

a = list(range(1, 11))
b = list(itertools.accumulate(a))
c = list(itertools.accumulate(a, func=operator.mul))

print(a)
print(b)
print(c)

# 出力結果
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
```