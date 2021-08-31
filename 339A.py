formula = input()
listformula = [char for char in formula]
itssorted = []

def sortlist(alist):
    sortedlist = []
    for val in alist[::2]:
        sortedlist.append(int(val))
    nowsorted = sorted(sortedlist)
    for val in nowsorted:
        itssorted.append(str(val))

sortlist(listformula)
print('+'.join(itssorted))
