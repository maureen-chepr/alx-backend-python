#!/usr/bin/env python3
""" duck-typed annotations """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Func that returns correct duck typed ann"""
    if lst:
        return lst[0]
    else:
        return None
