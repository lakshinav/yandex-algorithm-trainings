# I. Сапер

# можно использовать массив сдвигов

n,m,k = tuple(map(int, input().split()))

bomb = []
for _ in range(k):
    bomb.append(tuple(map(int, input().split())))

field = [[0 for _ in range(m)] for _ in range(n)]
for b in range(k):
    i, j = bomb[b]
    field[i-1][j-1] = '*'

for i in range(n):
    for j in range(m): # clockwise
        if field[i][j] != '*':
            if i-1 >= 0 and field[i-1][j] == '*':
                field[i][j] += 1
            if i-1 >= 0 and j+1 < m and field[i-1][j+1] == '*':
                field[i][j] += 1
            if j+1 < m and field[i][j+1] == '*':
                field[i][j] += 1
            if i+1 < n and j+1 < m and field[i+1][j+1] == '*':
                field[i][j] += 1
            if i+1 < n and field[i+1][j] == '*':
                field[i][j] += 1
            if  i+1 < n and j-1 >= 0 and field[i+1][j-1] == '*':
                field[i][j] += 1
            if j-1 >= 0 and field[i][j-1] == '*':
                field[i][j] += 1
            if i-1 >= 0 and j-1 >= 0 and field[i-1][j-1] == '*':
                field[i][j] += 1        
    print(*field[i])
