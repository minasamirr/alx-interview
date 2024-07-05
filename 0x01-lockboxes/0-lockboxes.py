#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < n and key not in opened:
                    stack.append(key)

    return len(opened) == n
