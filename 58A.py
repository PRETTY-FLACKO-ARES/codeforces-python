string = input()
hello = 'hello'

def findhello(string, string2):
    pos = 0
    for i in range(0, len(string)):
        if string[i] == string2[pos]:
            pos += 1
        if pos == 5:
            return 'YES'
    return 'NO'

print(findhello(string, hello))