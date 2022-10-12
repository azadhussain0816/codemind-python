a = int(input())
b = list(map(int,input().split()))
c = set(b)
k = 0
for i in c:
    if i%2==1:
        k+=1
print(k)
        