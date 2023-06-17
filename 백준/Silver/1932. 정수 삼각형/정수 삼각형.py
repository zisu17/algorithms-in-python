cnt=int(input())
triangle=[]
for i in range(cnt):
    triangle.append(list(map(int, input().split())))
dp = [[0] * i for i in range(1, len(triangle) + 1)]
for i in range(len(triangle) - 1, -1, -1):
    for j in range(i + 1):
        if i == len(triangle) - 1:
            dp[i][j] = triangle[i][j]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])
max_sum = dp[0][0]
print(max_sum)