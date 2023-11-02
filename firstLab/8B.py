n, m = map(int, input().split())
weights = [int(i) for i in input().split()]
values = [int(i) for i in input().split()]

dp = [[0 for x in range(m + 1)] for x in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if weights[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
result = []
i = n
j = m
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    else:
        result.append(i)
        j -= weights[i - 1]
        i -= 1

print(len(result))
answer = list(reversed(result))
for i in range(len(result)):
    print(str(answer[i]) + " ", end='')
