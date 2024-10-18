#!/usr/bin/python3
"""
Function module
"""


def makeChange(coins, total):
    """
    Function that returns the fewest number of coins needed to meet
    a given amount total

    Args:
        coins(list): list of coins
        total(int): total amount

    Returns:
        fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coins_count = 0

    for coin in coins:
        if total == 0:
            break

        if coin <= total:
            coins_count += total // coin
            total = total % coin

    if total > 0:
        return -1

    return coins_count
