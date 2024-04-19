#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list): A list of lists representing the locked boxes.
                      Each inner list contains the keys present in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set(boxes[0])
    visited = set([0])

    while keys:
        key = keys.pop()
        if key < len(boxes):
            visited.add(key)
            keys.update(set(boxes[key]) - visited)

    return len(visited) == len(boxes)
