initial = input().split()
initial = [int(i) for i in initial]

def plugitin(value, ntimes):
    number = value
    inter = ntimes
    while inter > 0:
        if number % 10 == 0:
            a = str(number)
            a = a[:-1]
            a = int(a)
            number = a
        else:
            number -= 1

        inter -= 1

    return number

print(plugitin(initial[0], initial[1]))