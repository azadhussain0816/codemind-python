a = int(input())
b = list(map(int,input().split()))
k = []
for i,j in zip(range(a//2),range(a-1,a//2-1,-1)):
    k.extend([b[i],b[j]])
if a%2==1:
    k.extend([b[a//2],0])
print(*k)
