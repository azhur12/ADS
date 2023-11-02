n, m = map(int, input().split())
bars = [int(i) for i in input().split()]
dp = [[False for x in range(m + 1)] for x in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = True
for i in range(1, m + 1):
    dp[0][i] = False
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if bars[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - bars[i - 1]]


w = 0
for i in bars:
    w+=i
if w < m:
    print(w)
else:
    while not dp[n][m]:
        m-=1
    print(m)