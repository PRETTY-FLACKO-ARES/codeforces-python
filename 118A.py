stringword = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

listword = [char for char in stringword]
novowels = []

def removevowels(alist):
    for i in alist:
        if i not in vowels:
            novowels.append(i)

removevowels(listword)

withperiod = []
def addperiod(alist):
    for i in novowels:
        withperiod.append('.')
        withperiod.append(i)

addperiod(novowels)

finalstr = ''.join(withperiod)

print(finalstr)
