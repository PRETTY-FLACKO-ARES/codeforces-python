initial = input()

upper = 0
lower = 0
for char in initial:
    if char.isupper() == True:
        upper += 1
    else:
        lower += 1

if upper > lower:
    print(initial.upper())
else:
    print(initial.lower())