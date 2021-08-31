initial = int(input())

counter = 0
magnetlist = []
for i in range(initial):
    magnet = int(input())
    magnetlist.append(magnet)


if len(magnetlist) > 0:
    counter += 1
    for i in range(initial-1):
        if magnetlist[i] != magnetlist[i+1]:
            counter += 1

print(counter)