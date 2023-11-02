def antiquick(N):
    perm = []
    i = N
    while i > 0:
        perm.append(i)
        i -= 1
    return perm


n = int(input())
result = antiquick(n)
for i in range(n):
    print(result[i], sep= " ", end = " ")
