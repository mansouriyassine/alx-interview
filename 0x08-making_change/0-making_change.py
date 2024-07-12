#!/usr/bin/python3
"""
0. Change comes from within
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given total
    using the provided coins.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

        if total == 0:
            return count

    return -1
