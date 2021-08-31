initial = input().split()
initial = [int(i) for i in initial]

def numofyears(weight1, weight2):
    counter = 0
    limak = weight1
    bob = weight2
    while limak <= bob:
        limak = limak * 3
        bob = bob * 2
        counter += 1
    return counter

print(numofyears(initial[0], initial[1]))