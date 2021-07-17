# D. Клавиатура

n = int(input())
button_life = list(map(int, input().split()))
k = int(input())
seq = list(map(int, input().split()))

for s in seq:
    button_life[s-1] -= 1

for bl in button_life:
    print('YES') if bl < 0 else print('NO')
     
