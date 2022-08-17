N = int(input())
mod = 10 ** 9 + 7
ans = 0
# 0~9
c_09 = (10 ** N) % mod

# 1~9
c_19 = (9 ** N) % mod

# 0~8
c_08 = (9 ** N) % mod

# 1~8
c_18 = (8 ** N) % mod

print((c_09 - c_08 - c_19 + c_18) % mod)
