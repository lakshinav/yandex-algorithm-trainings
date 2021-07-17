# G. Банковские счета

d = {}
with open('input.txt', 'r', encoding = 'utf-8') as infile:
    for line in infile:
        operation = line.split()
        if operation[0] == 'DEPOSIT':
            if operation[1] in d:
                d[operation[1]] += int(operation[2])
            else:
                d[operation[1]] = int(operation[2])
        elif operation[0] == 'BALANCE':
            if operation[1] in d:
                print(d[operation[1]])
            else:
                print('ERROR')
        elif operation[0] == 'WITHDRAW':
            if operation[1] in d:
                d[operation[1]] -= int(operation[2])
            else:
                d[operation[1]] = -int(operation[2])
        elif operation[0] == 'TRANSFER':
            if operation[1] not in d:
                d[operation[1]] = 0
            elif operation[2] not in d:
                d[operation[2]] = 0
            d[operation[1]] -= int(operation[3])
            d[operation[2]] += int(operation[3])
        elif operation[0] == 'INCOME':
            for name in d:
                if d[name] > 0:
                    d[name] = int(d[name]*(1+int(operation[1])/100))
