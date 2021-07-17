# C. Ближайшее число

n = int(input())
seq = list(map(int, input().split()))
x = int(input())

for i in range(n):
    seq[i] = seq[i]-x
min_cur = 2001
i_cur = 0
for i in range(n):
    tmp = abs(seq[i]) # lose information while taking abs
    if tmp < min_cur:
        min_cur = tmp
        i_cur = i
print(seq[i_cur]+x)
