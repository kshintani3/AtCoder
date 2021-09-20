# AtCoder Beginner Contest 189
## D - Logical Expression
- `ans`にはyiがTrueになる組み合わせが格納されており、
    - 文字列が`AND`の時は`xi="True"`かつ`yi-1="True"`のみなので組み合わせの数は変わらない。
    - 文字列が`OR`の時は
        1. `xi="True"`であれば、`yi-1`はどちらでもいいので、`i-1`までに考えられる全ての組み合わせ
        2. `xi="False"`であれば、`yi-1="True"`でないといけないので一つ前の組み合わせの数と同じ