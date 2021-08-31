initial = input().split()
initial = [int(i) for i in initial]

lineup = input()
lineup = [str(i) for i in lineup]

def doaswap(list, pos1, pos2):
    if list[pos1] == 'B' and list[pos2] == 'G':
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return True
    else:
        return False

def ladiesfirst(list1, list2):
    numberofchildren = list1[0]
    time = list1[1]
    queue = list2
    n = 0
    pos1 = 0
    pos2 = 1

    while n < time:
        for i in range(numberofchildren):
            if pos2 <= numberofchildren - 1:
                checker = doaswap(queue, pos1, pos2)
                if checker == True:
                    pos1 += 2
                    pos2 += 2
                else:
                    pos1 += 1
                    pos2 += 1

        n += 1
        pos1 = 0
        pos2 = 1

    return queue

print(''.join(ladiesfirst(initial, lineup)))
