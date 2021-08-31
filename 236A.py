username = input()

uniquename = ''.join(set(username))

def checkgender(str):
    if len(str) % 2 == 1:
        return 'IGNORE HIM!'
    elif len(str) % 2 == 0:
        return 'CHAT WITH HER!'

print(checkgender(uniquename))
