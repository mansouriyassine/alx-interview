#!/usr/bin/python3

"""
A script to determine if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """

    def is_start_byte(byte):
        """Check if the given byte is a valid start byte."""
        return (byte >> 7) == 0b0 or \
               (byte >> 5) == 0b110 or \
               (byte >> 4) == 0b1110 or \
               (byte >> 3) == 0b11110

    def is_continuation_byte(byte):
        """Check if the given byte is a continuation byte."""
        return (byte >> 6) == 0b10

    i = 0
    while i < len(data):
        byte = data[i]
        if not is_start_byte(byte):
            return False
        num_bytes = 0
        if (byte >> 7) == 0b0:
            num_bytes = 1
        elif (byte >> 5) == 0b110:
            num_bytes = 2
        elif (byte >> 4) == 0b1110:
            num_bytes = 3
        elif (byte >> 3) == 0b11110:
            num_bytes = 4
        else:
            return False
        if i + num_bytes > len(data):
            return False
        for j in range(i + 1, i + num_bytes):
            if not is_continuation_byte(data[j]):
                return False
        i += num_bytes
    return True