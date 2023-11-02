n, m = map(int, input().split())
bars = [int(i) for i in input().split()]
w = 0
for i in range(n):
    w += bars[i]
dp = [[False]*(w) for i in range(n)]
dp[0][0] = True
for i in range(1,n):
    dp[i][bars[0]] = True
for i in range(1,n):
    for j in range(w):
        if (j - bars[i]) >= 0:
            dp[i][j] = dp[i-1][j] or dp[i - 1][j - bars[i]]
        else:
            dp[i][j] = dp[i-1][j]

if w < m:
    print(w)
else:
    while not dp[n-1][m]:
        m-=1

    print(m)