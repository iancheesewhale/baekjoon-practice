import sys
k, n = map(int, sys.stdin.readline().split())
lns = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(lns)

result = 0

while start<= end:
    mid = (start + end) // 2
    count = 0
    for ln in lns:
        count += ln // mid
    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)