# AtCoder Beginner Contest 181
## D - Hachi
- `collections.Counter(a)` : `a`に含まれる要素と出現回数を格納
```python:
import collections

s = "ababaccdaa"
s_count = collections.Counter(s)
print(s_count["a"])
print(s_count)

# 出力結果
5
Counter({'a': 5, 'b': 2, 'c': 2, 'd': 1})
```
(補足) - Counter同士の演算も可能（要素数が0になると削除）
```python:
import collections

s1 = "ababaccdaa"
s2 = "acacbbcddd"
s_count1 = collections.Counter(s1)
s_count2 = collections.Counter(s2)
print(s_count1 - s_count2)
print(s_count2 - s_count1)

# 出力結果
Counter({'a': 3})
Counter({'d': 2, 'c': 1})
```