
n = int(input())

for i in range(n):
    val = input()
    if len(val) <= 10:
        print(val)
    else:
        print(val[0] + str(len(val[1:-1])) + val[-1])