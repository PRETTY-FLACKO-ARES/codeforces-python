initial = int(input())

lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

def almostlucky(int, list):
    for num in lucky:
        if int % num == 0:
            return 'YES'
    return 'NO'

print(almostlucky(initial, lucky))