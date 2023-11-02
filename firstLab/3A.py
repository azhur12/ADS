def binary_search(a, value):
    left = 0
    right = len(a) - 1
    if a[0] == value:
        return 1
    if a[right] == value:
        return right + 1
    while right - left > 1:
        index = (left + right) // 2
        if a[index] == value:
            return index + 1
        elif a[index] < value:
            left = index
        else:
            right = index

    return 0


n, m = map(int, input().strip().split(" "))
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
for i in range(m):
    result = (binary_search(a,b[i]))
    j = result - 1
    if result != 0:
        while b[i] == a[j]:
            j-=1
            if j < 0:
                break
        print(j + 2, end = " ")
        j = result - 1
        while b[i] == a[j]:
            j+=1
            if j == len(a):
                break
        print(j)
    else:
        print(result)

