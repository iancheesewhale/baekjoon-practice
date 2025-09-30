A, B = map(int, input().split())
arr = []
for i in range(1, B+1):
    for j in range(i):
        arr.append(i)
        if len(arr) >= B:
            break
    if len(arr) >= B:
        break
print(sum(arr[A-1:B]))