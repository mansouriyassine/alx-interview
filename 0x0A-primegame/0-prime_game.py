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

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task

Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins

GitHub repository: alx-interview
Directory: 0x0A-primegame
File: 0-prime_game.py
"""

def sieve_of_eratosthenes(max_n):
    """
    Sieve of Eratosthenes algorithm to find all prime numbers up to max_n.
    
    Parameters:
    - max_n: Maximum number up to which prime numbers are found.
    
    Returns:
    - List of prime numbers up to max_n.
    """
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if (is_prime[p] == True):
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_n + 1) if is_prime[p]]
    return prime_numbers

def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.
    
    Parameters:
    - x: Number of rounds.
    - nums: List of integers n for each round.
    
    Returns:
    - Name of the player that won the most rounds ('Maria' or 'Ben').
      If the winner cannot be determined, return None.
    """
    max_n = max(nums)
    prime_numbers = sieve_of_eratosthenes(max_n)
    
    dp = [False] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        dp[i] = False
        for prime in prime_numbers:
            if prime > i:
                break
            if not dp[i - prime]:
                dp[i] = True
                break
    
    wins = {"Maria": 0, "Ben": 0}
    
    for n in nums:
        if dp[n]:
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1
    
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
