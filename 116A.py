numstops = int(input())

mincap = 0
current = 0

for i in range(0, numstops):
    currentstop = input().split()
    currentstop = [int(x) for x in currentstop]

    current -= currentstop[0]
    current += currentstop[1]
    if current > mincap:
        mincap = current

print(mincap)