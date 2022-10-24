for i in range(int(input())):
    a = int(input())
    c = a
    b = 0
    while a>0:
        r = a%10
        b = b*10+r
        a = a//10
    print(c==b)