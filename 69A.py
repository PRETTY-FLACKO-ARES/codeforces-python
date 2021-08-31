numberofinput = int(input())

leftvector = []
midvector = []
rightvector = []

def putitin(alist):
    for i in range(0, alist):
        newvector = input().split()
        newvector = [int(x) for x in newvector]
        leftvector.append(newvector[0])
        midvector.append(newvector[1])
        rightvector.append(newvector[2])

def checkifitsin(alist):
    if sum(alist) == 0:
        return True
    else:
        return False

putitin(numberofinput)

if checkifitsin(leftvector) == True:
    if checkifitsin(midvector) == True:
        if checkifitsin(rightvector) == True:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')