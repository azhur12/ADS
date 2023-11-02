n = int(input())
s = input()

proseka = [0]*n

for i in range(n):
    if s[i] == '.':
        proseka[i] = 0
    elif s[i] == 'w':
        proseka[i] = -1
    elif s[i] == '"':
        proseka[i] = 1


dp = [0] * n
dp[0] = 0
for i in range(1,n):

    if proseka[i] == -1:
        dp[i] = -1
        continue
    if i - 3 < 0:
        if dp[i - 1] == -1:
            dp[i] = -1
            continue
        dp[i] = proseka[i] + dp[i-1]
    elif i - 5 < 0:
        if dp[i-1] == -1:
            if dp[i -3] == -1:
                dp[i] = -1
            else:
                dp[i] = proseka[i] + dp[i -3]
        if dp[i - 3] == -1:
            dp[i] = proseka[i] + dp[i - 1]
        else:
            dp[i] = proseka[i] + max(dp[i - 1], dp[i - 3])
    else :
        var = max(dp[i - 1], dp[i - 3], dp[i - 5])
        if var == -1:
            dp[i] = -1
        else:
            dp[i] = proseka[i] + var


print(dp[-1])