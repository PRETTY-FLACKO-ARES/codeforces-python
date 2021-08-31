lines = int(input())
submissions = 0

for i in range(0, lines):
    team = input().split()
    count = 0
    for people in team:
        if int(people) == 1:
            count += 1
    if count >= 2:
        submissions += 1

print(submissions)