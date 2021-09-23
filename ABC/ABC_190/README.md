# AtCoder Beginner Contest 190
## B - Magic 3
- `sys.exit()` : プログラム自体を終了させることができる。
## C - Bowls and Dishes
- `a = set()` :  重複しない要素のコレクション
- `itertools.product` : 複数のリストの直積。各リストから1つずつ選ぶ場合の全ての組み合わせ
```python:
入力
# 1 2
# 1 3
# 3 4

import itertools

a = [map(int, input().split()) for _ in range(3)]
b = itertools.product(*a)
for i in b:
    print(i)

# 出力結果
(1, 1, 3)
(1, 1, 4)
(1, 3, 3)
(1, 3, 4)
(2, 1, 3)
(2, 1, 4)
(2, 3, 3)
(2, 3, 4)
```