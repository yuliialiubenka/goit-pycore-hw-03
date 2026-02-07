import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """
    Generate a set of unique random numbers for lottery tickets.

    Args:
        min_num: Minimum possible number (must be >= 1)
        max_num: Maximum possible number (must be <= 1000)
        quantity: How many numbers to generate (between min_num and max_num)

    Returns:
        A sorted list of unique random integers. Returns empty list if invalid.

    Example:
        >>> get_numbers_ticket(1, 49, 6)
        [4, 15, 23, 28, 37, 45]
    """

    if not all(isinstance(value, int) for value in (min_num, max_num, quantity)):
        return []

    range_size = max_num - min_num + 1
    is_valid = 1 <= min_num <= max_num <= 1000 and 1 <= quantity <= range_size

    if not is_valid:
        return []
    return sorted(random.sample(range(min_num, max_num + 1), quantity))


# For testing purposes
if __name__ == "__main__":
    MIN_VALUE = 1
    MAX_VALUE = 1000
    QUANTITY_VALUE = 6

    lottery_numbers = get_numbers_ticket(MIN_VALUE, MAX_VALUE, QUANTITY_VALUE)
    print("Your lottery numbers:", lottery_numbers)
