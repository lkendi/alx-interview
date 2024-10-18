#!/usr/bin/python3
"""Prime game module"""


def sieve_of_eratosthenes(limit):
    """
    Finds all prime numbers up to a given limit using the
    Sieve of Eratosthenes algorithm.

    Function approach:
    First, assume all numbers are prime.
    Mark 0 and 1 as non-prime (since they are not prime).
    Iterate through numbers from 2 to the square root of the limit.
    If the current number is marked as prime,
    mark all its multiples as non-prime.

    Args:
        limit (int): The upper bound to find primes up to.

    Returns:
        list: A list of booleans, where True indicates
        the index is a prime number.
    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """
    Determines the winner between Maria and Ben in the prime number game.

    Function approach:
    For each round, find the prime numbers up to the given limit using the
    sieve function.
    Both players take turns removing a prime and its multiples.
    Track the number of turns.
    Maria wins if the number of turns is odd,
    Ben wins if the number of turns is even.
    After all rounds, the player with more wins is declared the overall winner.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers where each represents
                the limit of consecutive numbers for that round.

    Returns:
        str or None: The name of the player with the most wins,
        or None if no clear winner.
    """
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    for n in nums:
        primes_to_n = [i for i in range(2, n + 1) if primes[i]]

        turn = 0

        while primes_to_n:
            prime = primes_to_n.pop(0)

            primes_to_n = [p for p in primes_to_n if p % prime != 0]
            turn += 1

        if turn % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
