a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
k = 0
while len(a) != 0 and len(b) != 0:
    a_hand = a.pop(0)
    b_hand = b.pop(0)
    if (a_hand == 9 and b_hand == 0) or (a_hand == 0 and b_hand == 9):
        if a_hand == 9:
            b.append(a_hand)
            b.append(b_hand)
        else:
            a.append(a_hand)
            a.append(b_hand)
    else:
        if a_hand > b_hand:
            a.append(a_hand)
            a.append(b_hand)
        else:
            b.append(a_hand)
            b.append(b_hand)

    k += 1
    if k == 10 ** 6:
        break

if k == 10**6:
    print("botva")
else:
    if len(a) == 0:
        print("second" + " " + str(k))
    else:
        print("first" + " " + str(k))
