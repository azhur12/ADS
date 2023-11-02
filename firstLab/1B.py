
n, a0, k = map(int, input().strip().split(" "))
a = [a0]
for i in range(1, n):
    a.append((1103515245 * a[i - 1] + 12345) % (2 ** 31))

left = 0
right = len(a)
while True:
    mid = (left + right)//2
    i = left
    j = right - 1
    while a[i] < a[mid]:
        i+=1
    while a[j] > a[mid]:
        j-=1
    if i <= j:
        a[i], a[j] = a[j], a[i]
        i+=1
        j-=1
    if mid == k:
        print(a[mid])
        break
    elif k < mid:
        right = mid
    else:
        left = mid + 1


