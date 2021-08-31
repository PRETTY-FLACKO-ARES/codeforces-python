initial = str(input())
initial = [int(i) for i in initial]

luckynums = [4, 7]


def nearlylucky(list1, list2):
    counter = 0
    for number in list1:
        if number in list2:
            counter += 1

    for val in luckynums:
        if val == counter:
            return 'YES'

    return 'NO'

print(nearlylucky(initial, luckynums))