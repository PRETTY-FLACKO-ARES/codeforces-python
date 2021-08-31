
alist = input().split()
n, k = list(map(int, alist))

contestants = input().split()
contestants = [int(i) for i in contestants]

advance = 0
counter = 0

for i in range(0, k):
    if i <= k and contestants[i] != 0:
        advance += 1

for value in contestants[k:]:
    if value == contestants[k-1] and value != 0:
        advance += 1

print(advance)