#!/usr/bin/python3
from collections import deque


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
