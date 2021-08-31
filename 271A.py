uniqueyear = int(input()) #1987

def nextuniqueyear(integer):
    nextone = integer + 1 #1989
    while True:
        nextonelist = str(nextone)
        nextonelist = [int(str(i)) for i in nextonelist]
        if len(set(nextonelist)) == len(nextonelist):
            return nextone
        else:
            nextone += 1

print(nextuniqueyear(uniqueyear))