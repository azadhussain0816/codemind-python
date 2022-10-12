a = int(input())
b = list(map(int,input().split()))
if a%2==1:
    b.append(0)
print(*b)