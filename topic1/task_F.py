# F. Расстановка ноутбуков

tmp = list(map(int, input().split()))

a1=tmp[0]
b1=tmp[1]
a2=tmp[2]
b2=tmp[3]

sides1 = [a1+a2, a1+a2, a1+a2, a1+b2, a1+b2, a1+b2, a1+0, a1+0, b1+a2, b1+a2, b1+a2, b1+b2, b1+b2, b1+b2, b1+0, b1+0, 0+a2, 0+b2]
sides2 = [b1+b2, b1+0, 0+b2, a2+b1, a2+0, 0+b1, a2+b1, b1+b2,   a1+b2, b2+0, 0+a1, a1+a2, a2+0, 0+a1, a1+a2, a1+b2,   a1+b2,a2+b1]

s_cur = 0
s = a1*b1+a2*b2
i_opt = []
s_opt = []
for i in range(len(sides1)):
    s_cur = sides1[i]*sides2[i]
    if s_cur >= s:
        s_opt.append(s_cur)
        i_opt.append(i)
i_opt = i_opt[s_opt.index(min(s_opt))]
print(sides1[i_opt], sides2[i_opt])
