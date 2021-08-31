numgames = input()
outcome = input()
"""
def whowon(string):
    anton = 0
    danik = 0

    for char in string:
        if char == 'A':
            anton += 1
        else:
            danik += 1

    if anton > danik:
        return 'Anton'
    elif anton == danik:
        return 'Friendship'
    else:
        return 'Danik'


print(whowon(outcome))
"""
count = outcome.count('A')
print('Anton' if count > len(outcome)/2 else 'Friendship' if count == len(outcome)/2 else 'Danik')
