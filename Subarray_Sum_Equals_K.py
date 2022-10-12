a, b = map(int,input().split())
c = list(map(int,input().split()))
d = 0
for i in range(a):
    for j in range(i+1,a+1):
        if sum(c[i:j]) == b:
            d+=1
print(d)