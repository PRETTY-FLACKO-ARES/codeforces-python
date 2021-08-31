initial = int(input())
secondary = [5, 4, 3, 2, 1]

def calculatesteps(int, list):
    friendhouse = int
    diffsteps = list
    counter = 0
    while friendhouse > 0:
        if friendhouse - diffsteps[0] >= 0:
            friendhouse -= diffsteps[0]
            counter += 1
        elif friendhouse - diffsteps[1]>= 0:
            friendhouse -= diffsteps[1]
            counter += 1
        elif friendhouse - diffsteps[2] >= 0:
            friendhouse -= diffsteps[2]
            counter += 1
        elif friendhouse - diffsteps[3] >= 0:
            friendhouse -= diffsteps[3]
            counter += 1
        elif friendhouse - diffsteps[4] >= 0:
            friendhouse -= diffsteps[4]
            counter += 1
    return counter

print(calculatesteps(initial, secondary))
