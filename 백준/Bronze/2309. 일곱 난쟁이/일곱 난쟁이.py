short = []
for i in range(9):
    num = int(input())
    short.append(num)
total = sum(short)
for i in range(9):
    for j in range(i+1, 9):
        if short[i] + short[j] == total - 100:
            result = []
            for k in range(9):
                if k != i and k != j:
                    result.append(short[k])
            result.sort()
            for height in result:
                print(height)
            exit()