def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_1 = str(num1)
    num_2 = str(num2)
    sum_1 = 0
    sum_2 = 0
    for i in num_1:
        j = int(i)
        sum_1 += j
    for x in num_2:
        y = int(x)
        sum_2 += y
    if sum_1 == sum_2:
        return True
    else:
        return False
print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))