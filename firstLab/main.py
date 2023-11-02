def recsort(a):
    global k
    ln = len(a)
    if ln == 1:
        return a
    a1 = recsort(a[:ln // 2])
    a2 = recsort(a[ln // 2:])
    jk = len(a1 + a2)
    i = 0
    j = 0
    ln1 = len(a1)
    ln2 = len(a2)
    result = []
    while i + j < jk:
        if i == ln1:
            while i + j < jk:
                result.append(a2[j])
                j += 1
            break

        if j == ln2:
            while i + j < jk:
                result.append(a1[i])
                i += 1
            break
        if a1[i] <= a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1
            k += ln1 - i
    return result


n = int(input())
a = [int(i) for i in input().split()]
k = 0
result = recsort(a)
print(k)
