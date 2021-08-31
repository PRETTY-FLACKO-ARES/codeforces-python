initial = input()
initial = [str(i) for i in initial]
code = ['H', 'Q', '9']

def doesitwork(list1, list2):
    for val in list1:
        if val in list2:
            return 'YES'
    return 'NO'

print(doesitwork(initial,code))