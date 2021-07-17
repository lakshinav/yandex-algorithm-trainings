# A.Кондиционер

troom, tcond = tuple(map(int, input().split()))
mode = input()

if mode == 'fan':
    print(troom)
elif mode == 'auto':
   print(tcond)
elif mode == 'freeze' and tcond < troom:
   print(tcond)
elif mode == 'heat' and tcond > troom:
   print(tcond)
else:
   print(troom)
