n = int(input())
for i in range(n):
    print(chr(32) * (n - i - 1) + "*" * (i + 1))