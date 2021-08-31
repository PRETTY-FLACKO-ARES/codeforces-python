initial = input().split()
squad = input().split()

counter = 0
for person in squad:
    if int(person) <= int(initial[1]):
        counter += 1
    else:
        counter += 2

print(counter)