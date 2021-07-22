a = int(input())
b = int(input())
c = int(input())

l = 0
r = 4*10**15

while l < r:
    m = (l+r)//2
    if (2*a+3*b+4*c+5*m)*10 >= 35*(a+b+c+m):
        r = m
    else:
        l = m + 1
print(l)
