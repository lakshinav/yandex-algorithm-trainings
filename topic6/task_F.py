# F. Очень легкая задача

from math import lcm

#def lcm(a, b):
#    return abs(a*b) // gcd(a, b)

N, x, y = tuple(map(int, input().split()))

res = min(x,y) # first copy
xylcm = lcm(x,y)
qnt_of_copies_for_xylcm_sec = xylcm//x + xylcm//y
res += (N-1)//qnt_of_copies_for_xylcm_sec*xylcm
rest = (N-1)%qnt_of_copies_for_xylcm_sec
time_rest = 0
while rest > 0:
    time_rest += 1
    if time_rest%x == 0:
        rest -= 1
    if time_rest%y == 0:
        rest -= 1
print(res + time_rest)
