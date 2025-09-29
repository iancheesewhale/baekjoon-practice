n = int(input())
files = [input()for i in range(n)]

result = ''
for i in range(len(files[0])):
    char = files[0][i]
    same = True
    for j in range(1,n):
        if files[j][i] != char:
            same = False
            break
    if same:
        result += char
    else:
        result += '?'
print(result)