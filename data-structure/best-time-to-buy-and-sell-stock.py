from typing import *

def maxProfit_all_in_one(max_k: int, prices: List[int], cooldown: int, fee: int) -> int:
    n = len(prices)
    if n <= 0:
        return 0
    if max_k > n // 2:
        # 交易次数 k 没有限制的情况
        return maxProfit_k_inf(prices, cooldown, fee)

    dp = [[[0]*2 for _ in range(max_k+1)] for _ in range(n)]
    # k = 0 时的 base case
    for i in range(n):
        dp[i][0][1] = float('-inf')
        dp[i][0][0] = 0

    for i in range(n):
        for k in range(max_k, 0, -1):
            if i - 1 == -1:
                # base case 1
                dp[i][k][0] = 0
                dp[i][k][1] = -prices[i] - fee
                continue

            # 包含 cooldown 的 base case
            if i - cooldown - 1 < 0:
                # base case 2
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                # 别忘了减 fee
                dp[i][k][1] = max(dp[i - 1][k][1], -prices[i] - fee)
                continue
            dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
            # 同时考虑 cooldown 和 fee
            dp[i][k][1] = max(dp[i - 1][k][1], dp[i - cooldown - 1][k - 1][0] - prices[i] - fee)
    return dp[n - 1][max_k][0]


# k 无限制，包含手续费和冷冻期
def maxProfit_k_inf(prices: List[int], cooldown: int, fee: int) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    for i in range(n):
        if i - 1 == -1:
            # base case 1
            dp[i][0] = 0
            dp[i][1] = -prices[i] - fee
            continue

        # 包含 cooldown 的 base case
        if i - cooldown - 1 < 0:
            # base case 2
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 别忘了减 fee
            dp[i][1] = max(dp[i - 1][1], -prices[i] - fee)
            continue
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # 同时考虑 cooldown 和 fee
        dp[i][1] = max(dp[i - 1][1], dp[i - cooldown - 1][0] - prices[i] - fee)
    return dp[n - 1][0]