n = int(input())
result = 1
two_count = 0

for i in range(1, n + 1):
    temp = i
    while temp % 2 == 0:
        two_count += 1
        temp //= 2
    while temp % 5 == 0:
        if two_count > 0:
            two_count -= 1
        temp //= 5
    
    result *= temp
    result %= 1000000000000

result *= pow(2, two_count, 1000000000000)

while result % 10 == 0:
    result //= 10

print(str(result)[-5:])