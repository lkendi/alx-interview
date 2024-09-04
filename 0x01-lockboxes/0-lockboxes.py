#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes: list) -> bool:
    """
    Function to determine if all boxes can be unlocked

    Args:
        boxes(list of lists): represents boxes with keys

    Returns:
        True  of all boxes can be unlocked, False otherwise
    """

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    keys = boxes[0]

    for key in keys:
        if key < num_boxes and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)
