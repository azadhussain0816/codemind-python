a = int(input())
b = list(map(int,input().split()))
s = sum(b)
if s%2==0:
    print(1)
else:
    print(0)