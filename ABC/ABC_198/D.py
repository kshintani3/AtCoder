import random
def rasuu(l):
    a = []
    for i in range(l):
        if i == 0:
            a.append(random.randint(1, 9))
        else:
            a.append(random.randint(0, 9))
    return a

def jusin(a):
    b = 0
    for i in range(len(a)):
        b += a[i] * (10**i)
    return b

def kai():
    s1 = list(input())
    s2 = list(input())
    s3 = list(input())
    lens1 = len(s1)
    lens2 = len(s2)
    lens3 = len(s3)
    while True:
        a = rasuu(lens1)
        b = rasuu(lens2)
        a_int = jusin(a)
        b_int = jusin(b)
        for m in range(lens1):
            for n in range(len2):
                if s1[m] == s2[n]:
                    a[m] = b[n]
        c_int = a_int + b_int
        c = c_int.split()
        kai = 1
        if len(c) != lens3:
            continue
        for m in range(lens3):
            flag = 0
            for n in range(len1):
                if s3[m] == s1[n] and c[m] != a[n]:
                    flag = 1
            for n in range(len2):
                if s3[m] == s2[n] and c[m] != b[n]:
                    flag = 1
            if flag == 1:
                kai = 0
                break
        if kai == 0:
            continue

kai()