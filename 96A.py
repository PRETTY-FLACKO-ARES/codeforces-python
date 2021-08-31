lineup = input()

def checkup(str):
    if '0000000' in str:
        return 'YES'
    elif '1111111' in str:
        return 'YES'
    else:
        return 'NO'

print(checkup(lineup))