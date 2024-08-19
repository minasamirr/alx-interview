def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of integers representing the values of
        coins available.
        total (int): The target amount for which we need to find the
        fewest number of coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             - Returns 0 if the total is 0 or less.
             - Returns -1 if the total cannot be met by any combination
             of the coins.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0

    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count = total // coin
            total -= coin * count
            coin_count += count

    if total != 0:
        return -1

    return coin_count
