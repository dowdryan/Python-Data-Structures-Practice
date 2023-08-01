def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    sum = 0
    for num in range(start, len(nums)):
        sum += nums[num]
        if end is not None and num >= end:
            return sum
    return sum

print(sum_range([1, 2, 3, 4]))
print(sum_range([1, 2, 3, 4], 1))
print(sum_range([1, 2, 3, 4], end=2))
print(sum_range([1, 2, 3, 4], 1, 3))
print(sum_range([1, 2, 3, 4], 1, 99))