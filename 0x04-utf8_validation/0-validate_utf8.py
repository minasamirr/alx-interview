#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): The data set to be validated, where each integer
        represents a byte.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    for num in data:
        # Mask to get the least significant 8 bits
        num = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1's in the first byte
            if (num >> 5) == 0b110:
                n_bytes = 1
            elif (num >> 4) == 0b1110:
                n_bytes = 2
            elif (num >> 3) == 0b11110:
                n_bytes = 3
            elif (num >> 7) == 0:
                continue
            else:
                return False
        else:
            # Check if the byte is of form 10xxxxxx
            if (num >> 6) != 0b10:
                return False
        n_bytes -= 1

    return n_bytes == 0
