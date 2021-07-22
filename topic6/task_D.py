params = tuple(map(int, input().split()))

def rbinsearch(l, r, check, checkparams):
    while l != r:
        m = (l+r+1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return r

def check(d, params):
    n,a,b,w,h = params
    return (h//(a+2*d))*(w//(b+2*d)) >= n or (w//(a+2*d))*(h//(b+2*d)) >= n

print(rbinsearch(0, 10**18, check, params))
