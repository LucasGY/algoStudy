def knapsack(W: int, wt: List[int], val: List[int]) -> int:
    N = len(wt)
    # base case 已初始化
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if w - wt[i-1] < 0:
                # 这种情况下只能选择不装入背包
                dp[i][w] = dp[i - 1][w]
            else:
                # 装入或者不装入背包，择优
                dp[i][w] = max(
                    dp[i - 1][w - wt[i-1]] + val[i-1], 
                    dp[i - 1][w]
                )
    return dp[N][W]