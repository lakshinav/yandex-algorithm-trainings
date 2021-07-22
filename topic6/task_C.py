w,h,n = tuple(map(int, input().split()))

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l+r)//2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def check(size, params):
    w,h,n = params
    return (size//w) * (size//h) >= n

print(lbinsearch(0, (w+h)*n, check, (w,h,n)))
