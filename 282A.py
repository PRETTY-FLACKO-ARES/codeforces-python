bit = int(input())
counter = 0

for i in range(0, bit):
    addminus = input()

    add = 0
    subtract = 0
    for i in range(0, len(addminus)):
        if addminus[i] == '+':
            add += 1
        elif addminus[i] == '-':
            subtract += 1

    if add == 2:
        counter += 1
    elif subtract == 2:
        counter -= 1

print(counter)