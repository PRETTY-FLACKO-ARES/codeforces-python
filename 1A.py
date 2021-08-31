import math

alist = input().split()
alist = [int(i) for i in alist]
sqrneed = 1

for i in range(0, len(alist)-1):
    updateit = math.ceil(alist[i]/alist[-1])
    sqrneed = sqrneed * updateit

print(sqrneed)