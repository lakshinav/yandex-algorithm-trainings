# A. Возрастает ли список?

seq = list(map(int, input().split()))

is_monot = True
for i in range(1,len(seq)):
    if seq[i-1] >= seq[i]:
        is_monot = False
        break
print('YES' if is_monot else 'NO')
