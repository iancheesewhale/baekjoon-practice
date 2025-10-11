l, r = map(int, input().split())
str_l = str(l)
str_r = str(r)

count = 0

if len(str_l) != len(str_r):
    print(0)
else:
    for i in range(len(str_l)):
        if str_l[i] == str_r[i]:
            if str_l[i] == '8':
                count += 1
        else:
            break
    print(count)
    