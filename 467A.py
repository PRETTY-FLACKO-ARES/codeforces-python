initial = int(input())

def countrooms(num):
    counter = 0
    for i in range(num):
        room = input().split()
        room = [int(i) for i in room]
        if room[1] - room[0] >= 2:
            counter += 1

    return counter

print(countrooms(initial))