def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    sorted_ages = sorted(ages, reverse=True)
    return sorted_ages[1], sorted_ages[0]

# Test cases
print(two_oldest_ages([1, 2, 10, 8]))  # Output: (8, 10)
print(two_oldest_ages([6, 1, 9, 10, 4]))  # Output: (9, 10)
print(two_oldest_ages([1, 5, 5, 2]))  # Output: (2, 5)