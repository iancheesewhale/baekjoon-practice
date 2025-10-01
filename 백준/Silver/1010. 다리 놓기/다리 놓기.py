import math

t = int(input())
def combination(m, n):
    return math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
for _ in range(t):
    n, m = map(int, input().split())
    result = combination(m, n)
    print(result)