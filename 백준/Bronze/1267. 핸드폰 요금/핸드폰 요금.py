n = int(input())
times = list(map(int, input().split()))
y_total = 0
m_total = 0
for time in times:
    y_total += (time // 30 + 1) * 10
    m_total += (time // 60 + 1) * 15
    
if y_total > m_total:
    print('M', m_total)
elif y_total < m_total:
    print('Y', y_total)
else:
    print('Y M', y_total)