#!/usr/bin/env python3
""" type-annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Func that takes a float multiplier as argument"""

    def mult(m: float) -> float:
        """Func that multiplies a float by multiplier"""
        return m * multiplier

    return mult
