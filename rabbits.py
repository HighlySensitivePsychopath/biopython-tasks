n = int(input())
k = int(input())

if(n==1 or n==2):
    print(1)

else:
    dp=n*[1]
    # dp to tablica n elementowa wypełniona jedynkami
    for i in range(2, n):
        dp[i]=dp[i-1]+dp[i-2]*k

    print(dp[n-1])