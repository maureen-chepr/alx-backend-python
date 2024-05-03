#!/usr/bin/env python3
""" type-annotated function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Func that returns sum of mxd list as a float"""
    return sum(mxd_lst)
