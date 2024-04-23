#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''Calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.

    Args:
        n (int): Target number of characters

    Returns:
        int: Minimum number of operations

    Note:
        If n is impossible to achieve, return 0
    '''
    if n <= 1:
        return 0

    clipboard = 1
    pasted_chars = 1
    operations = 0

    while pasted_chars < n:
        if n % pasted_chars == 0:
            clipboard = pasted_chars
            operations += 1

        pasted_chars += clipboard
        operations += 1

    return operations if pasted_chars == n else 0
