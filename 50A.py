boardsize = input().split()
boardsize = [int(i) for i in boardsize]

squares = boardsize[0] * boardsize[1]

if squares % 2 == 0:
    print(int(squares/2))
else:
    print(int((squares -1)/2))