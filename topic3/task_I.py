# I. Полиглоты

n = int(input())
most_popular = set()
most_long = set()

for i in range(n):
    m = int(input())
    cur_set = set()
    for j in range(m):
        cur_set.add(input())
    most_long |= cur_set
    if i == 0:
        most_popular |= cur_set
    else:
        most_popular &= cur_set
print(len(most_popular))
print(*most_popular, sep='\n')
print(len(most_long))
print(*most_long, sep='\n')
