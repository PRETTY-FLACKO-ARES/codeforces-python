initial = input()
initial = [str(i) for i in initial]
reversed = input()

def reverseit(list):
    checklist = []
    length = len(list)-1
    while length >= 0:
        checklist.append(list[length])
        length -= 1
    return ''.join(checklist)

if reverseit(initial) == reversed:
    print('YES')
else:
    print('NO')