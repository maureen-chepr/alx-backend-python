#!/usr/bin/env python3
""" annotation with appropriate types """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Func that return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
