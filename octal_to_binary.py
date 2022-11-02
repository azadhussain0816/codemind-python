a = input()
opt=0
l = len(a)
for i in a:
    l-=1
    opt+=(8**l)*int(i)
print(bin(opt)[2:])