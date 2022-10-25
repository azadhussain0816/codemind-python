a, b = map(int,input().split())
a = str(a)

c = a[:b]
d = a[-b:]
print(abs(int(c)-int(d)))