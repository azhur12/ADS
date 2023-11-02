n, m, p = map(int, input().split())
barrels = [int(i) for i in input().split()]
index = 0
answer = 0
fine = 0
break_out_flag = False
honey_lasts = False
while m > 0:
    if honey_lasts:
        answer += barrels[index]
        m -= 1
        index += 1
        if index == n:
            break
    else:
        while barrels[index] < p:
            index += 1
            if index == n:
                barrels.sort(reverse=True)
                honey_lasts = True
                index = 0
                break_out_flag = True
                break
        if break_out_flag:
            continue
        m -= barrels[index] // p
        if m < 0:
            fine = abs(m)
        answer += (barrels[index] // p) * p - fine * p
        fine = 0
        barrels[index] = barrels[index] % p
        index += 1
        if index == n:
            barrels.sort(reverse=True)
            honey_lasts = True
            index = 0

print(answer)