#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing byte data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    def check_bytes(num_bytes):
        """
        Check if the next 'num_bytes' bytes in 'data' form a valid UTF-8 character.
        """
        for i in range(index + 1, index + num_bytes + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    index = 0
    while index < len(data):
        if (data[index] >> 7) == 0b0:
            index += 1
        elif (data[index] >> 5) == 0b110 and check_bytes(1):
            index += 2
        elif (data[index] >> 4) == 0b1110 and check_bytes(2):
            index += 3
        elif (data[index] >> 3) == 0b11110 and check_bytes(3):
            index += 4
        else:
            return False
    return True
