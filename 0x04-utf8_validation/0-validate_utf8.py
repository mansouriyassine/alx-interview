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
            if not (j < len(data) and is_continuation_byte(data[j])):
                return False
        i += num_bytes
    return True


# Test cases
if __name__ == "__main__":
    # Test case 1
    data1 = [0b11100100, 0b10000101, 0b1101100]
    print(validUTF8(data1))

    # Test case 2
    data2 = [240, 188, 128, 167]
    print(validUTF8(data2))

    # Test case 3
    data3 = [235, 140]
    print(validUTF8(data3))

    # Test case 4
    data4 = [345, 467]
    print(validUTF8(data4))

    # Test case 5
    data5 = [250, 145, 145, 145, 145]
    print(validUTF8(data5))

    # Test case 6
    data6 = [0, 0, 0, 0, 0, 0]
    print(validUTF8(data6))

    # Test case 7
    data7 = []
    print(validUTF8(data7))

    # Test case 8 (Long data set, valid)
    data8 = [240, 144, 128, 128] * 10
    print(validUTF8(data8))

    # Test case 9 (Long data set, invalid)
    data9 = [240, 144, 128, 128] * 10 + [240, 144]
    print(validUTF8(data9))
