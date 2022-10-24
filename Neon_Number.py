a = int(input())
b = a**2
c = 0
while b>0:
    r = b%10
    c = c+r
    b = b//10
if a==c:
    print("Neon Number")
else:
    print("Not Neon Number")