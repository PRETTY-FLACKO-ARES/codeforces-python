numstone = input()
stonelay = input()


def checkstones(newstring):
    counter = 0
    for i in range(0, len(stonelay)-1):
        if stonelay[i] == stonelay[i+1]:
            counter += 1
    return counter

print(checkstones(stonelay))
