#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using the loop function to process data"""

def process_data(data):
    """Finding the sum and the average of the data in a tuple.

    Args:
        data(mixed): A list or tuple of numbers.

    Returns:
        tuple: The total sum of the data and the average of the data with
        floating point decimal.

    Examples:

        >>> process_data([1, 2, 3])
        (6, 2.0)

    """
    total = 0 
    for item in data:
        count += 1
        total = total + item

    avg = total/count
    return (total, float(avg))

