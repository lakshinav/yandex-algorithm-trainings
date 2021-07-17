# H. Метро

a = int(input())
b = int(input())
n = int(input())
m = int(input())

tmin = max(n+(n-1)*a, m+(m-1)*b)
tmax = min(a+n+n*a, b+m+m*b)

if tmin > tmax:
    print(-1)
else:
    print(tmin, tmax)
