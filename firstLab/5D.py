n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()]
dp = [ [0]*(m + 1) for i in range(n + 1)]
paths = [ [""]*(m + 1) for i in range(n + 1)]
for i in range(1,n + 1):
    for j in range(1,m + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            paths[i][j] = paths[i-1][j-1] + str(a[i-1]) + " "
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j-1])
            if dp[i - 1][j] < dp[i][j - 1]:
                paths[i][j] = paths[i][j-1]
            else:
                paths[i][j] = paths[i-1][j]


index = 0
jndex = 0
answer = 0
for i in range(1,n + 1):
    for j in range(1, m + 1):
        if dp[i][j] > answer:
            answer = dp[i][j]
            index = i
            jndex = j

print(answer)
print(paths[index][jndex])

