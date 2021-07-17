# E. Чемпионат по метанию коровьих лепешек

n = int(input())
seq = list(map(int, input().split()))

winner_points = max(seq)
winner_flag = False
vasya = []
for i in range(n-1):
    if winner_flag and seq[i]%10 == 5 and seq[i+1] < seq[i]:
        vasya.append(seq[i])
    if seq[i] == winner_points:
        winner_flag = True

if vasya:
    seq.sort(reverse=True)
    vasya = max(vasya)
    for i in range(n):
        if seq[i] == vasya:
            print(i+1)
            break
else:
    print(0)
