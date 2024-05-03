#!/usr/bin/env python3
""" type-annotated function sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Func that returns the sum of a list as a float"""
    return sum(input_list)
