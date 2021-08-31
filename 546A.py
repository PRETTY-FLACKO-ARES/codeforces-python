initial = input().split()
initial = [int(i) for i in initial]

def calculatecost(cost, numofban):
    totalcost = 0
    inter = numofban
    while inter > 0:
        totalcost += inter * cost
        inter -= 1

    return totalcost

findcost = calculatecost(initial[0], initial[2])

def dothemath(totalcost, ownmoney):
    if findcost - ownmoney <= 0:
        return 0
    else:
        return findcost-ownmoney

print(dothemath(findcost, initial[1]))