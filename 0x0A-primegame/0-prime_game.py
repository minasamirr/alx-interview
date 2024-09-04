#!/usr/bin/python3
"""
Prime Game - Determines the winner of a game based on prime numbers.
"""


def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.

    Parameters:
    x (int): The number of rounds.
    nums (list of int): The list of 'n' values for each round.

    Returns:
    str: The name of the player that won the most rounds.
    None: If the winner cannot be determined.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
