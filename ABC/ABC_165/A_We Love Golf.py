K = int(input())
A, B = map(int, input().split())
if A <= K * (B // K) or K * (A // K + 1) <= B:
    print("OK")
else:
    print("NG")
