matrix = []
for i in range(0, 5):
    matrix.append(input().split())

matrix = [[int(str) for str in list] for list in matrix]

counter = 0
rowpos = 1
for lists in matrix:
    gotit = 0
    for number in lists:
        if number == 1:
            gotit += 1
            break
    if gotit == 0:
        rowpos += 1
    else:
        break

if rowpos > 3:
    counter += rowpos - 3
elif rowpos < 3:
    counter += 3 - rowpos

colpos = 1
for val in matrix[rowpos-1]:
    if val == 1:
        break
    colpos += 1

if colpos > 3:
    counter += colpos - 3
elif colpos < 3:
    counter += 3- colpos

print(counter)