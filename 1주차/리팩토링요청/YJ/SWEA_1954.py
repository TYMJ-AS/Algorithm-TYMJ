t = int(input())

for j in range(1, t+1):
    a = int(input())
    lst = [[None for _ in range(a)] for _ in range(a)]
    x = 0
    y = 0

    count_1 = count_2 = count_3 = count_4 = 0
    count = 0
    i = 1

    while i <= a * a:
        if i == 1:
            lst[x][y] = i
            i += 1
            continue

        if count_1 < a - count:
            if y + 1 <= a - 1 and lst[x][y + 1] is None:
                y += 1
                lst[x][y] = i
                count_1 += 1
                i += 1
                continue
            else:
                count_1 += 1

        if count_2 < a - count:
            if x + 1 <= a - 1 and lst[x + 1][y] is None:
                x += 1
                lst[x][y] = i
                count_2 += 1
                i += 1
                continue
            else:
                count_2 += 1

        if count_3 < a - count:
            if y - 1 >= 0 and lst[x][y - 1] is None:
                y -= 1
                lst[x][y] = i
                count_3 += 1
                i += 1
                continue
            else:
                count_3 += 1

        if count_4 < a - count:
            if x - 1 >= 0 and lst[x - 1][y] is None:
                x -= 1
                lst[x][y] = i
                count_4 += 1
                i += 1
                continue
            else:
                count_4 += 1

        if count_1 and count_2 and count_3 and count_4:
            count_1 = count_2 = count_3 = count_4 = 0
            count += 1
    print(f'#{j}')
    for i in lst:
        print(*i)
    
