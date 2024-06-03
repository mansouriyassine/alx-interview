#!/usr/bin/python3

"""
0. Change comes from within

Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total.

Prototype:
    def makeChange(coins, total)

Returns:
    The fewest number of coins needed to meet the total.
    - If total is 0 or less, return 0.
    - If total cannot be met by any number of coins you have, return -1.

Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to be achieved using the fewest number
                 of coins.

Assumptions:
    - The value of a coin will always be an integer greater than 0.
    - You can assume you have an infinite number of each denomination of
      coin in the list.

Your solution’s runtime will be evaluated in this task.
"""

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given total
    using the provided coins.

    Args:
        coins (list): A list of the values of the coins in your
                      possession.
        total (int): The total amount to be achieved using the fewest
                     number of coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             - Returns 0 if total is 0 or less.
             - Returns -1 if total cannot be met by any number of coins
               you have.
    """
    if total < 0:
        return -1
    
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                min_coins[amount] = min(min_coins[amount],
                                        min_coins[amount - coin] + 1)
    
    return min_coins[total] if min_coins[total] != float('inf') else -1
