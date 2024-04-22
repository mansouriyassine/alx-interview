#!/usr/bin/python3
"""
Calculates the minimum number of operations needed
to achieve a given number of characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)
    return dp[n]
