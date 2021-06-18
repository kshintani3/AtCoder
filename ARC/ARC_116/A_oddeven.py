def yakusuu(sinp):

    odd = 0
    even = 0
    i = 1
    while i*i <= sinp:
        if sinp % i == 0:
            if i%2 == 0:
                even += 1
            else:
                odd += 1

            if i != sinp // i:
                if (sinp // i)%2 == 0:
                    even += 1
                else:
                    odd += 1
        i += 1

    if odd > even:
        print("Odd")
    elif odd < even:
        print("Even")
    else:    
        print("Same")

def main():
    import sys
    input = sys.stdin.readline
    t = int(input())
    s = [int(input().rstrip('\n')) for _ in range(t)]
    for i in range(t):
        print(yakusuu(s[i]))

main()