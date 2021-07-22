# G. Площадь

n = int(input())
m = int(input())
t = int(input())

l, r = 0, 10**9
def rbinsearch(l, r, check, checkparams): 
    while l != r:
        mid = (l+r+1)//2
        if check(mid, checkparams):
            l = mid
        else:
            r = mid-1
    return l

def check(width, params):
    n,m,t = params
    if 2*width >= n or 2*width >= m:
        return False
    return n*m-(n-2*width)*(m-2*width) <= t

print(rbinsearch(l, r, check, (n,m,t)))
