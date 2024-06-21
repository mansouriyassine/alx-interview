#!/usr/bin/python3
"""
Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n for each round.

    Returns:
    str: Name of the player that won the most rounds.
         If the winner cannot be determined, returns None.
    """
    if x <= 0 or not nums:
        return None

    def sieve(n):
        """Generate primes up to n using Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    max_n = max(nums)
    primes = sieve(max_n)

    def count_primes(n):
        """Count the number of primes up to n."""
        return sum(primes[:n+1])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n <= 1:
            ben_wins += 1
        else:
            prime_count = count_primes(n)
            if prime_count % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
