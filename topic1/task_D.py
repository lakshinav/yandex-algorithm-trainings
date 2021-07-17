# D. Уравнение с корнем

a = int(input())
b = int(input())
c = int(input())

if c < 0:
  print("NO SOLUTION")
else:
  if a == 0:
    if c*c == b:
      print("MANY SOLUTIONS")
    else:
      print("NO SOLUTION")
  else:
     xtmp = (c*c-b) 
     print(xtmp//a if xtmp%a == 0 else "NO SOLUTION")
