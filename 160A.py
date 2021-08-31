numcoins = input()
coinvalue = input().split()
coinvalue = [int(i) for i in coinvalue]
coinvalue = sorted(coinvalue, reverse=True)

def takeit(list):
    sumval = sum(list)
    currentval = 0
    takecoins = 0
    for coins in list:
        if currentval <= sumval/2:
            currentval += coins
            takecoins += 1
    return takecoins

print(takeit(coinvalue))