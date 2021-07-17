# J. Система линейных уравнений - 2

a,b,c,d,e,f = float(input()),float(input()),float(input()),float(input()),float(input()),float(input())
det = a*d-b*c
if det != 0:
    print(2, (e*d-b*f)/det, (a*f-c*e)/det)
elif a==0 and b==0 and c==0 and d==0 and e==0 and f==0:
    print(5)
elif (b!=0 and d!=0) and (a==0 and c==0) and (e/b == f/d):
    print(4, e/b)
elif (b!=0 and d==0) and (a==0 and c==0) and (f==0):
    print(4, e/b)
elif (d!=0 and b==0) and (a==0 and c==0) and (e==0):
    print(4, f/d)
elif (a!=0 and c!=0) and (b==0 and d==0) and (e/a == f/c):
    print(3, e/a)
elif (a!=0 and c==0) and (b==0 and d==0) and (f==0):
    print(3, e/a)
elif (a==0 and c!=0) and (b==0 and d==0) and (e==0):
    print(3, f/c)
elif ((c!=0 and d!=0 and f!=0) and (a/c == b/d and b/d == e/f)):
    print(1, -c/d, f/d)
elif ((a!=0 and b!=0 and e!=0) and (c/a == d/b and d/b == f/e)):
    print(1, -a/b, e/b)
elif (a!=0 or c!=0) and (b==0 and d==0 and e==0 and f==0):
    print(4, 0)
elif (b!=0 or d!=0) and (a==0 and c==0 and e==0 and f==0):
    print(3, 0)
elif a+c==0 and b+d==0 and e+f==0 and b!=0:
    print(1, -a/b, e/b)
elif a+c==0 and b+d==0 and e+f==0 and d!=0:
    print(1, -c/d, f/d)
else:
    print(0)
