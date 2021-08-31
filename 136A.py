numfriends = int(input())
gifting = input().split()
gifting = [int(i) for i in gifting]

def giftppl(list):
    neworder = []
    for i in range(1, numfriends+1):
        neworder.append(list.index(i) + 1)
    strver = [str(x) for x in neworder]
    return strver

print(' '.join(giftppl(gifting)))